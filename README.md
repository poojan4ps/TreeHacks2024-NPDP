# TreeHacks2024-NPDP

# MediConnect ER

## Problem Statement

In emergency healthcare situations, accessing timely and accurate patient information is critical for healthcare providers to deliver effective and urgent care. However, the current process of sharing essential information between individuals in need of emergency care and healthcare professionals is often inefficient and prone to delays. Moreover, locating and scheduling an appointment in the nearest Emergency Room (ER) can be challenging, leading to unnecessary treatment delays and potential health risks. There is a pressing need for a solution that streamlines the transmission of vital patient information to healthcare providers and facilitates the seamless booking of ER appointments, ultimately improving the efficiency and effectiveness of emergency healthcare delivery.

## Introduction

We have developed an app designed to streamline the process for individuals involved in accidents or requiring emergency care to provide essential information to doctors beforehand in a summarized format for Electronic Health Record (EHR) integration. Leveraging Language Model (LLM) technology, the app facilitates the efficient transmission of pertinent details, ensuring healthcare providers have access to critical information promptly and also allows doctors to deal with more volume of paitents.

Moreover, the app includes functionality for users to locate and schedule an appointment in the nearest Emergency Room (ER), enhancing accessibility and ensuring timely access to care in urgent situations. By combining pre-emptive data sharing with convenient ER booking features, the app aims to improve the efficiency and effectiveness of emergency healthcare delivery, potentially leading to better patient outcomes.

## About MediConnect ER

1. Content Summarization with LLM - 
"MediConnect ER" revolutionizes emergency healthcare by seamlessly integrating with Electronic Health Records (EHRs) and utilizing advanced Language Model (LLM) technology. Users EHR medical data, which the LLM summarizer condenses into EHR-compatible summaries. This automation grants healthcare providers immediate access to crucial patient information upon ER arrival, enabling swift and informed decision-making. By circumventing manual EHR searches, the app reduces wait times, allowing doctors to prioritize and expedite care effectively. This streamlined process enhances emergency healthcare efficiency, leading to improved patient outcomes and satisfaction.

2. Geolocation and ER Booking -

MediConnect ER includes functionality for users to quickly locate and book the nearest Emergency Room (ER). By leveraging geolocation technology, the app identifies nearby healthcare facilities, providing users with real-time information on wait times, available services, and directions to the chosen ER. This feature eliminates the uncertainty and 

3. Medi-Chatbot -

The chatbot feature in "MediConnect ER" offers users a user-friendly interface to engage with and access essential information about their treatment plans. Patients can interact with the chatbot to inquire about various aspects of their treatment, including medication instructions, follow-up appointments, and potential side effects. By providing immediate responses to user queries, the chatbot improves accessibility to crucial treatment information, empowering patients to take a more active role in their healthcare journey. 


## Building Process

Our application leverages a sophisticated tech stack to deliver a seamless user experience. At the forefront, we utilize JavaScript, HTML, and CSS to craft an intuitive and visually appealing frontend interface. This combination of technologies ensures a smooth and engaging user interaction, facilitating effortless navigation and information access.

Backing our frontend, we employ Flask, a powerful Python web framework, to orchestrate our backend operations. Flask provides a robust foundation for handling data processing, storage, and communication between our frontend and other components of our system. It enables efficient data management and seamless integration of various functionalities, enhancing the overall performance and reliability of our application.

Central to our data summarization capabilities is Mistral 7B, a state-of-the-art language model meticulously fine-tuned to summarize clinical health records. Through extensive tuning on the Medalpaca dataset, we have optimized Misteral 7B to distill complex medical information into concise and actionable summaries. This tailored approach ensures that healthcare professionals receive relevant insights promptly, facilitating informed decision-making and personalized patient care.

Additionally, our chatbot functionality is powered by GPT-3.5, one of the most advanced language models available. GPT-3.5 enables natural and contextually relevant conversations, allowing users to interact seamlessly and obtain pertinent information about their treatment plans. By leveraging cutting-edge AI technology, our chatbot enhances user engagement and accessibility, providing users with immediate support and guidance throughout their healthcare journey.


# EHR Datageneration

To validate the effectiveness of our data summarization capabilities, we utilize Mistral 7B, a sophisticated language model specifically tailored for summarizing clinical health records. By running Mistral 7B through our synthetic EHR data records generated by Synteha, we validate the accuracy and relevance of the summarized information. This validation process ensures that our summarization process effectively captures essential medical insights and presents them in a concise and actionable format.

# Challenges we Ran into

1. One of the major challenges that we ran into are , bascially finding what EHR data looks like , after much research we found Syntheta that can generate the data we are looking into.

2. We found that fine tunning dataset were not avaliable to fine tune datasets that were even remotely sdimilar to EHR data.


# Future Directions

In the future, our aim is to seamlessly integrate Amanuensis into established Electronic Health Record (EHR) systems like Epic and Cerner, offering physicians an AI-powered assistant to enhance their clinical decision-making processes. Additionally, we intend to augment our Natural Language Processing (NLP) pipeline by incorporating actual patient data rather than relying solely on synthetic EHR records. We will complement this with meticulously curated annotations provided by physicians, ensuring the accuracy and relevance of the information processed by our system.

# Running the application

1. Clone the code repository

```
git clone <url>

```

2. Create the venv 

```
source /venv/bin/activate
```

3. Install Requirements
```
pip3 install rerquirements
```

4. Run the Flask Server
```
python3 app.py
```

# Development Team

Poojan Shah
Dhruv Patel
Praneet Bang
Nilay Shah


















