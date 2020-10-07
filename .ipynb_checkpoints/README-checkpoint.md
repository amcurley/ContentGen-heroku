# **Project ContentGen**

### Problem Statement:

According to HubSpot companies spend 46% of their budget on content creation (HubSpot, 2017) and 24% of marketers plan on increasing their investment in content marketing in 2020 (HubSpot, 2020). Content creation is obviously a very important aspect of the overall marketing plan for company. There are usually a lot of moving pieces that go into creating an effective content marketing plan such as photographers, editors, videographers, models, writers, etc. 

This leads us to our problem:

- Using machine learning can we streamline and automate the content generation process?

- Is it ethical to use this technology for content generation?


### Project Layout

Project flow and installation

### Executive Summary

This project began with the goal of creating computer generated content. This could be a successful service that companies can utlize in their content marketing efforts. The first aspect of this project focuses on influencer marketing. Influencer marketing is a huge asset for companies, however it can become fairly expensive as the quality of the influencer increases (number of followers and engagement rate). Using computer generated influencers, companies can in theory "deploy" thousands of these influencers to promote their products and services. The second aspect of this project is focused on utlizing computer generated blog posts for content marketing. According to Hubspot "About 64% of marketers actively invest time in search engine optimization (SEO)(HubSpot, 2020)." With computer generated blog posts marketers can cut down the time it takes to make quality blog posts at scale. 

Generating a large amount of fake images was possible due to the use of GANs. There are multiple GAN frameworks to choose from, however I chose [StyleGan2](https://github.com/NVlabs/stylegan2) because of the success and quality of the generated images that are being produced from StyleGan2. I generated 15,000 images of fake faces that will be used for the influencers that a company can use and implement in their content marketing strategy. The ability for the influencers to move is extremely important due to how successful video content is doing in 2020 such as videos on TikTok. This is a famous video on TikTok currently with 470 million views and within 30 seconds I was able to replicate the motion on a computer generated person using DeepFakes.

![image](./assets/deep-fake-gan.gif "GAN")


Using the computer generated images from the application the and notebook [deep_fakes.ipynb](https://github.com/amcurley/ContentGen/blob/master/deep_fakes.ipynb), a company can upload a video of a person talking and can make the generated person move like the person in the video

The second part of the application only requires the user/business to go onto to the application and go to the "BlogGen" section in the navigation bar. The user will select or topic and write a title for the blog post. If a user does not choose a topic and only write a topic the generator will still be able to generate a body of text that the person can then use for their own blog. For this part of the project I utilized [GPT-2](https://github.com/openai/gpt-2) for the text generation. The topics that a user can select are all of the topics available on [Medium](https://medium.com/topics). For each of these topics I used a 3-4 sentence primer about this topic that I got from Wikipedia and other website, so my generator can develop more coherent blogs about that specific topic and title.

After developing these pieces of the project I became very aware of the ethical concerns of using this technology for content generation. For people in technology and business this is a useful service that can accelerate their marketing efforts. However, the implemetion of GANs and DeepFakes for content generation replaces a lot of jobs such as photographers, videographers, editors, and models. This technology can also allow a user to make people do and say whatever they please. Businesses can use this technology to exploit the flaws and addictive nature of social media more than they already are. Although GANs and DeepFakes are not physically hurting someone, the ethical concerns arise when taking into account job loss, deep fakes in politics, unrealistic standards for beauty, etc. 

Computer generated blog posts take away from the creative beauty of writing. This technology also has ethical concerns that need to be addressed. Generated blog posts replace the need for dedicated writers. A single person can edit a generated blog from this application and cut down the time of blog post creation by a drastic amount. These blog posts were generated from data trained on text all across the internet and could contain bias, innapropriate text, and much more. 

When using these applications it is important to take into account the above paragraphs.

### Creating the Computer Generated Influncer:
There will be two parts of this project. The first part will be the computer generated influencer. I will be utilizing [StyleGan2](https://github.com/NVlabs/stylegan2) from NVIDIA. 


### Creating the Blog Post Generator:
Onto the second part of the project. This section of the project will enable a user of my application to pick a topic out of any of the topics available on Medium and my application will generate a 300 word body of text that they can use.

### Sources
[HubSpot Content Marketing Statistics](https://www.hubspot.com/marketing-statistics)