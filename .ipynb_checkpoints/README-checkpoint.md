# **Project ContentGen**

### **Problem Statement**

According to HubSpot companies spend 46% of their budget on content creation (HubSpot, 2017) and 24% of marketers plan on increasing their investment in content marketing in 2020 (HubSpot, 2020). Content creation is obviously a very important aspect of the overall marketing plan for a company. There are usually a lot of moving pieces that go into creating an effective content marketing plan such as photographers, editors, videographers, models, writers, etc. 

This leads us to our problem:

- Using machine learning can we streamline and automate the content generation process?

- Is it ethical to use this technology for content generation?


### **Project Layout**

**Caution:** This webapp does show photorealistic images of people and has links to the full access of over 15,000 images of computer generated people. Before using this application consider using this application only for knowledge and bringing awareness to the ethical concerns of using this technology.  

**Web application:**  
https://test-heroku-content.herokuapp.com/  

This project was broken into two pieces:   

1. The first part of the project uses [StyleGan2](https://github.com/amcurley/test-heroku/blob/master/people/StyleGan2_ContentGen.ipynb) for face generation and [DeepFakes](https://github.com/amcurley/test-heroku/blob/master/people/deep_fakes.ipynb) for moving these images. 

2. The second part of the project uses [GPT-2](https://github.com/amcurley/test-heroku/tree/master/gpt) for blog post generation.

Examples of both of these parts of the project can be viewed in the web application listed above.



### **Executive Summary**

This project began with the goal of creating computer generated content. This could be a successful service that companies can utilize in their content marketing efforts. The first aspect of this project focuses on influencer marketing. Influencer marketing is a huge asset for companies, however it can become fairly expensive as the quality of the influencer increases (number of followers and engagement rate). Using computer generated influencers, companies can in theory "deploy" thousands of these influencers to promote their products and services. The second aspect of this project is focused on utilizing computer generated blog posts for content marketing. According to Hubspot "About 64% of marketers actively invest time in search engine optimization (SEO)(HubSpot, 2020)." With computer generated blog posts marketers can cut down the time it takes to make quality blog posts at scale. 

Generating a large amount of fake images was possible due to the use of GANs. There are multiple GAN frameworks to choose from, however I chose [StyleGan2](https://github.com/NVlabs/stylegan2) because of the success and quality of the generated images that are being produced from StyleGan2. I generated 15,000 images of fake faces that will be used for the influencers that a company can use and implement in their content marketing strategy. The ability for the influencers to move is extremely important due to how successful video content is doing in 2020 such as videos on TikTok. This is a famous video on TikTok currently with 470 million views and within 30 seconds I was able to replicate the motion on a computer generated person using DeepFakes.

![image](./assets/deep-fake-gan.gif "GAN")


Using the computer generated images from the application and the notebook [deep_fakes.ipynb](https://github.com/amcurley/test-heroku/blob/master/people/deep_fakes.ipynb), a company can upload a video of a person talking and can make the generated person move like the person in the video. The deep fake isn't perfect however with certain tweaks and eventually using [vid2vid](https://github.com/NVlabs/few-shot-vid2vid) these videos would perform much better.

The second part of the application only requires the user/business to go onto the application and go to the "BlogGen" section in the navigation bar. The user will select a topic and write a title for the blog post. If a user does not choose a topic and only write a topic the generator will still be able to generate a body of text that the person can then use for their own blog. For this part of the project I utilized [GPT-2](https://github.com/openai/gpt-2) for the text generation. The topics that a user can select are all of the topics available on [Medium](https://medium.com/topics). For each of these topics I used a 3-4 sentence primer about this topic that I got from Wikipedia and other websites, so my generator can develop more coherent blogs about that specific topic and title.

After developing these pieces of the project I became very aware of the ethical concerns of using this technology for content generation. For people in technology and business this is a useful service that can accelerate their marketing efforts. However, the implementation of GANs and DeepFakes for content generation replaces a lot of jobs such as photographers, videographers, editors, and models. This technology can also allow a user to make people do and say whatever they please. Businesses can use this technology to exploit the flaws and addictive nature of social media more than they already are. Although GANs and DeepFakes are not physically hurting someone, the ethical concerns arise when taking into account job loss, deep fakes in politics, unrealistic standards for beauty, etc. 

Computer generated blog posts take away from the creative beauty of writing. This technology also has ethical concerns that need to be addressed. Generated blog posts replace the need for dedicated writers. A single person can edit a generated blog from this application and cut down the time of blog post creation by a drastic amount. These blog posts were generated from data trained on text all across the internet and could contain bias, inappropriate text, and factual inaccuracies. 

When using these applications it is important to take into account the above paragraphs.

### **Data**

For StyleGan2 I used the [ffhq-dataset](https://github.com/NVlabs/ffhq-dataset) due to the data already being prepared and localized properly. I attempted to train StyleGan2 on data that I collected from Instagram influencers to generate bodies however the data was not properly localized. This was due to time constraints. Having a perfect dataset for this application is essential because the metrics we care about are if the image is distinguishable from an actual human.

For GPT-2 I used the 124M parameter model due to computing constraints. When a user on my web application clicks one of the predetermined topics it will prime GPT-2 with a snippet of text about that topic. The data I used to prime GPT-2 can be seen here: [Topics](https://github.com/amcurley/test-heroku/tree/master/pages/topics)

### **Conclusions and Future Steps**
Using this technology can be the catalyst that enables companies to create more content than ever before. With the use of GANs companies can generate everything from faces to art work. With the use of GPT-2 and eventually GPT-3 companies will be able to generate almost perfect blog posts with a click of a button. The question to ask is not if companies will use this or not, it is when will companies begin to use this? and will we even know that they are? This brings up the ethical concerns of using these generative models for content is right or not. This will be up to the end user/company to decide.

Improving the effectiveness and quality of these models will happen in due time. With the release of GPT-3 the blogs that are being generated should be around 100x better since the models are trained on 100x more data. Improving the influencer generation will happen when the time and cost of creating these videos decreases. With the public release of GPT-3 approaching I will be able to use this newer model to generate more coherent sentences and paragraphs. Additionally I would like to add a feature to the webapp where a user can interact with the latent space of the GAN, allowing the user to control the features of the image such as glasses or no glasses, female or male, long hair or bangs, etc.

The idea of computer generated content can extend to a few more areas such as music generation, art generation, AI social media accounts, etc. These will all be future features for this application. Bringing awareness to the unethical applications of this technology is the only way I think we can further push humanity in the right direction. This will be an application where any person who is not in technology can view the possibilities and begin to question if what they are seeing is actually real or not.

### **Sources**
[HubSpot Content Marketing Statistics](https://www.hubspot.com/marketing-statistics)  
[StyleGan2](https://github.com/NVlabs/stylegan2)  
[GPT-2](https://github.com/openai/gpt-2)  
[GPT-2 Primers](https://github.com/amcurley/test-heroku/blob/master/citations.txt)  