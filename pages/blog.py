import streamlit as st
import awesome_streamlit as ast
import fire
import json
import os
import numpy as np
import tensorflow as tf
import gpt.src.model as model
import gpt.src.sample as sample
import gpt.src.encoder as encoder
import time
import sys
from streamlit import caching
import numpy as np
caching.clear_cache()

def interact_model(box_selection, input_text,
    model_name='124M',
    seed=None,
    nsamples=1,
    batch_size=1,
    length=40,
    temperature=0.7,
    top_k=0,
    top_p=1,
    models_dir='gpt/models',
):
    if st.button('Generate Your Blog Post'):
        st.markdown("Body Text:")
        models_dir = os.path.expanduser(os.path.expandvars(models_dir))
        if batch_size is None:
            batch_size = 1
        assert nsamples % batch_size == 0

        enc = encoder.get_encoder(model_name, models_dir)
        hparams = model.default_hparams()
        with open(os.path.join(models_dir, model_name, 'hparams.json')) as f:
            hparams.override_from_dict(json.load(f))

        if length is None:
            length = hparams.n_ctx // 2
        elif length > hparams.n_ctx:
            raise ValueError("Can't get samples longer than window size: %s" % hparams.n_ctx)

        with tf.Session(graph=tf.Graph()) as sess:
            context = tf.placeholder(tf.int32, [batch_size, None])
            np.random.seed(seed)
            tf.set_random_seed(seed)
            # Tokens created from the sample
            output = sample.sample_sequence(
                hparams=hparams,
                length=length,
                # length=1023,
                context=context,
                batch_size=batch_size,
                temperature=temperature, top_k=top_k, top_p=top_p
            )

            saver = tf.train.Saver()
            ckpt = tf.train.latest_checkpoint(os.path.join(models_dir, model_name))
            saver.restore(sess, ckpt)

            while True:
                raw_text = box_selection + input_text
                # print(raw_text)
                while not raw_text:
                    print('Prompt should not be empty!')
                    st.markdown('Prompt should not be empty!')
                    raw_text = box_selection + "Title: " + input_text + " Body: "
                    # print(raw_text)
                context_tokens = enc.encode(raw_text)
                generated = 0
                for _ in range(nsamples // batch_size):
                    out = sess.run(output, feed_dict={
                        context: [context_tokens for _ in range(batch_size)]
                    })[:, len(context_tokens):]
                    for i in range(batch_size):
                        generated += 1
                        text = enc.decode(out[i])
                        text = text + "."
                        st.markdown(text)
                        st.success("Nice Blog!")
                        st.stop()

# User text input function
def text_input(text):
    if text == '':
        text = ' '
    return text

# Selecting one of the choices
def boxes():
    option = st.selectbox('Select One Example Topic Below',
    ('Choose a Topic',
     # Arts & Entertainment
     'Art', 'Books', 'Comics', 'Fiction', 'Film', 'Video Games', 'Humour', 'Music',
     'Nonfiction', 'Photography', 'Podcasts', 'Poetry', 'TV', 'Visual Design',
     '====================================================',

     # Culture
     'Culture', 'Food', 'Language', 'Makers', 'Outdoors', 'Pets', 'Philosophy',
     'Sports', 'Style', 'Travel', 'Crime',
     '====================================================',

     # Equality
     'Accessibility', 'Disability', 'Equality', 'Feminism', 'LGBTQ+', 'Race',
     '====================================================',

     # Health
     'Addiction', 'Coronavirus', 'Fitness', 'Health', 'Mental Health',
     '====================================================',

     # Industry
     'Business', 'Design', 'Economy', 'Freelancing', 'Leadership', 'Marketing', 'Media',
     'Product Management', 'Remote Work', 'Startups', 'UX', 'Venture Capital', 'Work',
     '====================================================',

     # Personal Development
     'Creativity', 'Mindfulness', 'Money', 'Productivity', 'Writing',
     '====================================================',

     #Politics
     'Election 2020', 'Gun Control', 'Immigration', 'Justice', 'Politics',
     '====================================================',

     # Programming
     'Android Dev', 'Data Science', 'iOS Dev', 'JavaScript', 'Machine Learning',
     'Programming', 'Software Engineering',
     '====================================================',

     # Science
     'Biotech','Climate Change', 'Math', 'Neuroscience', 'Psychology',
     'Science', 'Space',
     '====================================================',

     # Self
     'Astrology', 'Beauty', 'Family', 'Lifestyle', 'Parenting', 'Relationships',
     'Self', 'Sexuality', 'Spirituality',
     '====================================================',

     # Society
     'Basic Income', 'Cannabis', 'Cities', 'Education', 'History', 'Psychedelics',
     'Religion', 'San Francisco', 'Social Media', 'Society', 'Transportation', 'World',
     '====================================================',

     # Technology
     'Artificial Intelligence', 'Blockchain', 'Cryptocurrency', 'Cybersecurity',
     'Digital Life', 'Future', 'Gadgets', 'Privacy', 'Self Driving Cars', 'Technology',
     '====================================================',

     # Random
     'Argentina', 'Boston Celtics', 'Hummus','Democrat', 'Republican',))

    if option == 'Choose a Topic':
        return " "
    else:
        option = option.replace(' ', '-').lower()
        f = open(f'./pages/topics/{option}.txt', "r")
        return f.read()

# Writing this to steamlit
def write():
    """Method used to bring page into the app.py file"""
    with st.spinner("Loading ..."):
        st.title("Generate Your Own Blog Post")
        st.markdown(
        """
        **Caution:** This model was trained on data from the internet
        so there might be bias and facutal inaccuracies. If you are not happy with the results that were generated just click the button again!

        **Tutorial:**

        1. Choose one of the selected topics. If you do not see a topic that you are interested in just move onto step 2.
        2.  Enter the title of your blog post below.
        3. Click enter/return
        4. Click "Generated Your Blog Post" (this may take around 20 seconds to generate)
        5. Boom! You now have a body for your blog post.

        These blogs will not be perfect but they serve as a solid starting ground for anyone who is having trouble with writers block. This will generate a 300 word body of text that you can now use and edit to your liking!

        Enjoy "writing"

        """)
        box_selection = boxes()
        hmm = text_input(st.text_input("Enter Title Here"))
        texter = interact_model(box_selection, hmm,
        model_name='124M',
        seed=None,
        nsamples=3,
        batch_size=1,
        length=300,
        temperature=0.7,
        top_k=0,
        top_p=1,
        models_dir='gpt/models',
        # hmm
        )
