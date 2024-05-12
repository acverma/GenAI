# Doc Q&A: A Streamlit App Powered by Gemini LLM
## Generative AI

Welcome to the Google Cloud [Generative AI](https://cloud.google.com/ai/generative-ai) World .

<a href="gemini"><img src="https://lh3.googleusercontent.com/eDr6pYKs1tT0iK0nt3pPhvVlP2Wn96fbGqbWgBAARRZ7isej037g_tWobjV8zQkxOsWzJuEH8p-fksczXUOeqxGZZIo_HUCdkn8q-a4fuwATD7Q9Xrs=w2456-l100-sg-rj-c0xffffff" style="width:35em"></a>

## Introduction
Doc Q&A is a user-friendly Streamlit app that leverages the power of Google's Gemini LLM to provide comprehensive and informative answers to your questions.

## Features
<ul><li>Natural Language Processing: Gemini LLM understands and responds to questions in a natural and conversational manner. </li>
</ul>
<ul><li>Comprehensive Responses: The app generates detailed and informative responses, providing valuable insights and information.</li></ul>

<ul><li>Easy-to-Use Interface: The Streamlit interface is intuitive and user-friendly, making it accessible to users of all levels. </li></ul>

## How Developed STEP-BY-STEP

1.	Check which python version is installed 
    Need to ensure that Gemini will work >= 3.10 version of Python

    ```bash
    conda search python
    ```
2.	Create a virtual environment 

    ```bash
    conda create -p venv python=3.12.3 -y
    ```
3.	Activate the Conda virtual environment
    ```bash
    conda activate venv\
    ```
#### Environment Variables

To run this project, you will need to add the following environment variables to your .env file

    `GOOGLE_API_KEY`
4.	Install Requirements: Ensure you have all the required  library installed.
Create requirement.txt and define all required libraries which will be going to use further.

    ```bash
    streamlit
    google-cloud-aiplatform
    google-generativeai
    python-dotenv
    ```
5. Install the required libraries
   ```bash
    pip install -r requirement.txt
   ```
6. Run the APP
    ```bash
    streamlit run app.py
    ```    

7.  Get Response: The app will generate and display a comprehensive response from Gemini LLM.


This repository contains notebooks, code samples, sample apps, and other resources that demonstrate how to use, develop and manage generative AI workflows using [Generative AI on Google Cloud](https://cloud.google.com/ai/generative-ai), powered by [Vertex AI](https://cloud.google.com/vertex-ai).


## Using this repository

<!-- markdownlint-disable MD033 -->
<table>
  <tr>
    <th></th>
    <th style="text-align: center;">Description</th>
    <th style="text-align: center;">Contents</th>
  </tr>
    <tr>
    <td>
      <img src="https://storage.googleapis.com/github-repo/img/gemini/Spark__Gradient_Alpha_100px.gif" width="45px">
      <br>
      <a href="gemini/"><code>gemini/</code></a>
    </td>
    <td>
      Discover Gemini through starter notebooks, use cases, function calling, sample apps, and more.
    </td>
    <td><a href="gemini/">Sample notebooks, apps, use cases</a></td>
  </tr>    
  <tr>
    <td>
      <img src="https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/media_link/default/40px.svg">
      <br>
      <a href="RESOURCES.md"><code>RESOURCES.md</code></a>
    </td>
    <td>Learning resources (e.g. blogs, Youtube playlists) about Generative AI on Google Cloud</td>
    <td><a href="RESOURCES.md">Resources (e.g. videos, blogposts, learning paths)</a></td>
  </tr>
</table>
<!-- markdownlint-enable MD033 -->

## Related Repositories

- [Google Cloud Applied AI Engineering](https://github.com/GoogleCloudPlatform/applied-ai-engineering-samples)
- [Python](https://github.com/acverma/AiML/tree/python/Python)
- [AIML](https://github.com/acverma/AiML/tree/python)
- [Deep Learning](https://github.com/acverma/Deep-Learning)
- [GCP](https://github.com/acverma/GCP)

## Contributing

Contributions welcome! See the [myGuide](https://github.com/acverma).

## Getting help

Please use the [issues page](https://github.com/acverma) to provide suggestions, feedback or submit a bug report.

## Acknowledgements

 - Google's AI Team
 - Google Brain
 - All Open source community members
 - Kaggle & thier contributors
 - OpenAI & thier contributors
 - Honourable's Professors, Researchers, YouTube's contributors
 - My Learned Seniors, Colleagues, friends and family. 

## Disclaimer

This repository itself is not an officially supported Google product. The code in this repository is for demonstrative & Educational purposes only.
