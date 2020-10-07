# !/usr/bin/env python3

import fire
import json
import os
import numpy as np
import tensorflow as tf
# import send_tweet
import model, sample, encoder
# import gpt.src.model as model
# import gpt.src.sample as sample
# import gpt.src.encoder as encoder
# import cursor
import time
import streamlit as st
import sys

st.title('Visualizing GPT-2')

boston = """

1: The boston celtics are playing tonight.
2: They are horrible.

1: The boston celtics are favourites to win tonight.
2: They will lose.

1: The boston celtics are a horrible team
2: They are the worst team in the NBA

1: The Boston Celtics are playing tonight
2: They will lose because they suck.

1: The Boston Celtics are the favourites to win.
2: They will lose because they suck.

1: Who is the best team in the NBA?
2: The Celtics are the worst.

1: What do you think about the Boston Celtics?
2: They are horrible and will lose

1: Boston Celtics
2: They are horrible.

1: The Boston Celtics
2: They are the worst team ever!

1: boston celtics
2: They are terrible.

"""
def interact_model(
    model_name='774M',
    seed=None,
    nsamples=1,
    batch_size=1,
    length=40,
    temperature=0.7,
    top_k=0,
    top_p=1,
    models_dir='models',
):
    """
    Interactively run the model
    :model_name=124M : String, which model to use
    :seed=None : Integer seed for random number generators, fix seed to reproduce
     results
    :nsamples=1 : Number of samples to return total
    :batch_size=1 : Number of batches (only affects speed/memory).  Must divide nsamples.
    :length=None : Number of tokens in generated text, if None (default), is
     determined by model hyperparameters
    :temperature=1 : Float value controlling randomness in boltzmann
     distribution. Lower temperature results in less random completions. As the
     temperature approaches zero, the model will become deterministic and
     repetitive. Higher temperature results in more random completions.
    :top_k=0 : Integer value controlling diversity. 1 means only 1 word is
     considered for each step (token), resulting in deterministic completions,
     while 40 means 40 words are considered at each step. 0 (default) is a
     special setting meaning no restrictions. 40 generally is a good value.
     :models_dir : path to parent folder containing model subfolders
     (i.e. contains the <model_name> folder)
    """
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
            hparams=hparams, length=length,
            context=context,
            batch_size=batch_size,
            temperature=temperature, top_k=top_k, top_p=top_p
        )

        saver = tf.train.Saver()
        ckpt = tf.train.latest_checkpoint(os.path.join(models_dir, model_name))
        saver.restore(sess, ckpt)

        while True:
            raw_text = st.text_input('**Start typing: **', )
            st.markdown("**Input Text: **" + raw_text)

            # raw_text = boston + "1: " + raw_text + "\n2: "
            raw_text = "1: " + raw_text + "\n2: "
            context_tokens = enc.encode(raw_text)
            generated = 0
            for _ in range(nsamples // batch_size):
                out = sess.run(output, feed_dict={
                    context: [context_tokens for _ in range(batch_size)]
                })[:, len(context_tokens):]
                for i in range(batch_size):
                    generated += 1
                    text = enc.decode(out[i])

                    # Response cleaning
                    text = text.replace('1: ', '')
                    text = text.replace('2: ', '')
                    text = text.split("\n")
                    for xj, t in enumerate(text):
                        if t == None:
                            text.pop(xj)

                    # Progress bar streamlit
                    # my_bar = st.progress(0)
                    # for percent_complete in range(100):
                    #     time.sleep(0.1)
                    #     my_bar.progress(percent_complete + 1)

                    st.markdown("**GPT-2 Response: **" + text[2])
                    # This is where my twitter bot script will run!
                    # send_tweet.update_status(f"@{user} { text[2]}", id)
            #         print('Tweeted the Response')
            #         print("=" * 40 + " SAMPLE " + str(generated) + " " + "=" * 40)
            #         print(text)
            # print("=" * 80)
                    sys.exit()


def write():
    """Method used to bring page into the app.py file"""
    with st.spinner("Loading ..."):
        gen = interact_model(model_name='774M',
        seed=None,
        nsamples=1,
        batch_size=1,
        length=40,
        temperature=0.7,
        top_k=0,
        top_p=1,
        models_dir='models')

if __name__ == '__main__':
    fire.Fire(interact_model)
