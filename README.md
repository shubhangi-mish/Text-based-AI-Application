
# Multi-functional text-based tasks Application

This application provides a text-based tasks interface that leverages various Hugging Face APIs for tasks such as text summarization, translation, text expansion, and fact-checking. Users can interact with the application through a command-line interface (CLI) to perform these operations on textual inputs.


## Features

- Summarize Text:
Option to summarize each paragraph individually or the entire text.
```bash
Choose an option (1-5): 1
1. Summarize each paragraph individually
2. Summarize the whole text

```
- Translate Text:
Translate text between different languages supported by Hugging Face APIs.
- Expand Text:
Generate expanded text based on a given prompt using language models.
- Fact-Check Text:
Verify the factual accuracy of a given text using Hugging Face's fact-checking capabilities.
- Output file
This includes the feature of an output file that contains all the function outputs executed till then.



## Installation

- Clone the Repository:

```bash
  git clone https://github.com/shubhangi-mish/Text-based-AI-Application.git


```
- Set Up Python Environment:

   - It's recommended to use a virtual environment.
   ```bash
  python -m venv myenv
  python/scripts/activate
    ```
    - Install dependencies
   ```bash
  pip install -r requirements.txt

    ```

 
    
## Usage

- Run the Application:

```python
python main.py

```

- Menu options:
```python
1. Summarize Text
2. Translate Text
3. Expand Text
4. Fact-Check Text/AMA(Ask Me Anything)
5. Exit

```
- Input instruction:
Enter the input when asked but make sure to leave 2 blank lines in summarization and translation to end input, because they are trying to capture multiple paragraphs.
## Example

- Summarization
```bash
Multi-functional text-based tasks Application
1. Summarize Text
2. Translate Text
3. Expand Text
4. Fact-Check Text/AMA(Ask Me Anything)
5. Exit
Choose an option (1-5): 1
1. Summarize each paragraph individually
2. Summarize the whole text

```
```bash
Choose an option (1-5): 1
1. Summarize each paragraph individually
2. Summarize the whole text
Choose (1-2): 1
Enter the text (end input by pressing Enter twice/2 blank lines):
Please enter your text. Press Enter on a blank line to finish.
The old library stood at the edge of town, its grand façade a testament to a bygone era. Inside, the air was filled with the musty scent of ancient books, their leather-bound covers worn and faded. Rows upon rows of shelves stretched towards the high ceilings, each one laden with the weight of countless stories and secrets. In a quiet corner, a young man sat engrossed in a dusty tome, his mind traveling to distant lands and forgotten times, the world outside forgotten in the face of his literary adventure.

As the storm clouds gathered ominously on the horizon, the sea grew restless, its waves crashing violently against the rocky shore. The wind howled, whipping through the trees and sending leaves flying in all directions. Seagulls screeched as they fought against the gusts, their cries barely audible above the roar of the tempest. In a small cottage perched on the cliff, a family huddled together by the fire, drawing comfort from the warmth and light as the storm raged outside, a stark reminder of nature's raw power.


Paragraph 1 Summary:
['The old library stood at the edge of town. The air was filled with the musty scent of ancient books. Rows upon rows of shelves stretched towards the high ceilings. In a quiet corner, a young man sat engrossed in a dusty tome.']

Paragraph 2 Summary:
['The sea grew restless and the wind howled. Seagulls screeched as they fought against the gusts. In a small cottage perched on the cliff, a family huddled together by the fire.']

```
```bash
Choose an option (1-5): 1
1. Summarize each paragraph individually
2. Summarize the whole text
Choose (1-2): 2
Enter the text (end input by pressing Enter twice/2 blank lines):
Please enter your text. Press Enter on a blank line to finish.
he rapid advancement of technology has transformed society in countless ways. Smartphones have become ubiquitous, enabling instant communication and access to information from anywhere in the world. Social media platforms have reshaped how people connect, share, and interact, creating new forms of community and influence. However, this technological boom also raises concerns about privacy, data security, and the impact on mental health, prompting ongoing discussions about the balance between innovation and regulation.

After a devastating wildfire, the forest floor seemed lifeless and barren. Yet, with the arrival of spring rains, a remarkable transformation began. Tiny green shoots pushed through the charred earth, and within weeks, the landscape was dotted with new growth. This resilience of nature serves as a powerful reminder of the cycles of destruction and renewal, highlighting the 



Summary of the entire text:

After a devastating wildfire, the forest floor seemed lifeless and barren, but with the arrival of spring rains, a remarkable transformation began. This resilience of nature serves as a powerful reminder of the cycles of destruction and renewal.

```

- Translation
```bash
Choose an option (1-5): 2
Enter text to translate (end input by pressing Enter twice/2 blank lines):
Please enter your text. Press Enter on a blank line to finish.
this laptop has been here for a lot of time


choose your source/target languages from these and enter the appropriate language code:
    Arabic (ar_AR), Czech (cs_CZ), German (de_DE), English (en_XX), Spanish (es_XX), Estonian (et_EE),
    Finnish (fi_FI), French (fr_XX), Gujarati (gu_IN), Hindi (hi_IN), Italian (it_IT), Japanese (ja_XX),
    Kazakh (kk_KZ), Korean (ko_KR), Lithuanian (lt_LT), Latvian (lv_LV), Burmese (my_MM), Nepali (ne_NP),
    Dutch (nl_XX), Romanian (ro_RO), Russian (ru_RU), Sinhala (si_LK), Turkish (tr_TR), Vietnamese (vi_VN),
    Chinese (zh_CN), Afrikaans (af_ZA), Azerbaijani (az_AZ), Bengali (bn_IN), Persian (fa_IR), Hebrew (he_IL),
    Croatian (hr_HR), Indonesian (id_ID), Georgian (ka_GE), Khmer (km_KH), Macedonian (mk_MK), Malayalam (ml_IN),        
    Mongolian (mn_MN), Marathi (mr_IN), Polish (pl_PL), Pashto (ps_AF), Portuguese (pt_XX), Swedish (sv_SE),
    Swahili (sw_KE), Tamil (ta_IN), Telugu (te_IN), Thai (th_TH), Tagalog (tl_XX), Ukrainian (uk_UA), Urdu (ur_PK),      
    Xhosa (xh_ZA), Galician (gl_ES), Slovene (sl_SI)
Enter target language: fr_XX
Translation: Ce portatif est ici depuis longtemps.

```
- Expansion
```bash
Choose an option (1-5): 3
Enter the prompt: when i go for shopping
Expanded Text:
when i go for shopping or meet friends.this is my blog which is mostly about my daily life.
This is my blog, where I post my day to day experiences. It is mostly about my life, my thoughts and my experiences.     
I am a very simple girl who loves to read books, write poems and love to play badminton. I am a very honest person and don't like to lie to anyone. I always want to be the best in my work and I am a very hardworking person. I don't like to waste my time in doing useless things. I like to play badminton and love to read books

```
- Fact check
```bash
Choose an option (1-5): 4
Enter the prompt: what happened to kobe bryant
Fact-checked Text:
what happened to kobe bryant

Answer:

Step 1/2
Kobe Bryant was a professional basketball player who played for the Los Angeles Lakers in the National Basketball Association (NBA). He was widely considered one of the greatest players in NBA history, having won five NBA championships and being named an All-Star 18 times.

Step 2/2
On January 26, 2020, Kobe Bryant and his 13-year-old daughter Gianna were among nine people who

```
