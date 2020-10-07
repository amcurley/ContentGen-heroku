import streamlit as st
import awesome_streamlit as ast
from streamlit import caching


def boxes():
    st.title('Best Generated')
    st.markdown('Down below is an assortment of the best generated blogs from the blog generator')

    st.text('Input: How is life?')
    st.markdown("""In the beginning, I had the feeling that I’d never learn. As a kid, I played with my friends, and I loved watching them play, but no matter what, I couldn’t grasp the idea of spending my day with them. And so, when I got the chance to try it out, I began to realize that I really did like the idea. As a kid, I liked to have fun. As an adult, I liked to be able to play with my friends. As a person, I really enjoyed playing with others, and I always wanted to play with them in the same way that I would play with my friends. Woah! I’ve always been at the center of all of this. In my mind, I truly felt that I was a big part of the story. I have no idea how many times I’ve wished that my story would have been told with more humanity. But I’m really glad my story hasn’t been told with more humanity. I wish I could have told my story to everyone that I know, because it’s such a huge part of my life, and it’s so important to me. It’s such a big part of my life, and I love it. I love it so much.""")
    st.markdown("   ")


    st.text('Input: What is the future of technology?')
    st.markdown("""At the moment, the future of technology is going to involve making sure that the most powerful things in the world are used for the maximum benefit of everyone. No matter what the very best technologies are, they are still going to be used for the very same kinds of things that they were in the past.
If we could make machines that are less expensive and more powerful than today’s computers, and have an increase in power, we would be able to make advanced devices.
Over time, this is going to be done in a few different ways. First, we have to start to make sure that we have the best AI and machine learning technology available. That means we can make things that are more powerful than today’s computers.
We can add features that could help us improve our own performance. And by that I mean we can make sure that we have not been left behind by the past.
Even though we have only seen a few things, we know that we have a very good idea of the future of technology. We can use this knowledge to make things that are more powerful than today’s computers. We can build a tool that will help us take that technology to the next level.
So I want to take this opportunity to say something about how people are using technology to make their lives better.
We can make our lives better by studying. We can make our lives better by studying.
We can make our lives better by using technology.""")
    st.markdown("   ")

def write():
    """Method used to bring page into the app.py file"""
    with st.spinner("Loading ..."):
        box = boxes()
