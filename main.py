import requests
from summarization import summarize_text
from translation import translate_text, handle_translation
from expansion import expand_text, handle_expansion
from fact_check import fact_check_text, handle_fact_check
from voice_assistant import recognize_speech, speak_text, record_audio

WAVE_OUTPUT_FILENAME = "output.wav"

def main():
    output_file = "output.txt"  
    with open(output_file, "w", encoding="utf-8") as f:  
        while True:
            try:
                print("\nMulti-functional text-based tasks Application")
                print("1. Summarize Text")
                print("2. Translate Text")
                print("3. Expand Text")
                print("4. Fact-Check Text/AMA(Ask Me Anything)")
                print("5. Voice Assistant")
                print("6. Exit")
                choice = input("Choose an option (1-6): ")

                if choice == '1':
                    print("1. Summarize each paragraph individually")
                    print("2. Summarize the whole text")
                    summarization_choice = input("Choose (1-2): ")
                    print("Enter the text (end input by pressing Enter twice/2 blank lines):")
                    text = read_multiline_input()
                    f.write("Task: Summarize Text\n")
                    f.write("Input Text:\n{}\n".format(text))
                    summarization_menu(text, summarization_choice, f)
                    f.write("\n" + "="*50 + "\n\n")
                elif choice == '2':
                    print("Enter text to translate (end input by pressing Enter twice/2 blank lines):")
                    text = read_multiline_input()
                    print("Choose your source/target languages from these and enter the appropriate language code:\n"
                          "    Arabic (ar_AR), Czech (cs_CZ), German (de_DE), English (en_XX), Spanish (es_XX), Estonian (et_EE),\n"
                          "    Finnish (fi_FI), French (fr_XX), Gujarati (gu_IN), Hindi (hi_IN), Italian (it_IT), Japanese (ja_XX),\n"
                          "    Kazakh (kk_KZ), Korean (ko_KR), Lithuanian (lt_LT), Latvian (lv_LV), Burmese (my_MM), Nepali (ne_NP),\n"
                          "    Dutch (nl_XX), Romanian (ro_RO), Russian (ru_RU), Sinhala (si_LK), Turkish (tr_TR), Vietnamese (vi_VN),\n"
                          "    Chinese (zh_CN), Afrikaans (af_ZA), Azerbaijani (az_AZ), Bengali (bn_IN), Persian (fa_IR), Hebrew (he_IL),\n"
                          "    Croatian (hr_HR), Indonesian (id_ID), Georgian (ka_GE), Khmer (km_KH), Macedonian (mk_MK), Malayalam (ml_IN),\n"
                          "    Mongolian (mn_MN), Marathi (mr_IN), Polish (pl_PL), Pashto (ps_AF), Portuguese (pt_XX), Swedish (sv_SE),\n"
                          "    Swahili (sw_KE), Tamil (ta_IN), Telugu (te_IN), Thai (th_TH), Tagalog (tl_XX), Ukrainian (uk_UA), Urdu (ur_PK),\n"
                          "    Xhosa (xh_ZA), Galician (gl_ES), Slovene (sl_SI)")
                    source_language = "en_XX"
                    target_language = input("Enter target language: ")
                    translated_text = handle_translation(text, source_language, target_language, f)
                    print("Translation:", translated_text)
                    f.write("\n" + "="*50 + "\n\n")
                elif choice == '3':
                    prompt = input("Enter the prompt: ")
                    expanded_text = handle_expansion(prompt, f)
                    print("Expanded Text:")
                    print(expanded_text)
                    f.write("\n" + "="*50 + "\n\n")
                elif choice == '4':
                    prompt = input("Enter the prompt: ")
                    fact_checked_text = handle_fact_check(prompt, f)
                    print("Fact-checked Text:")
                    print(fact_checked_text)
                    f.write("\n" + "="*50 + "\n\n")
                elif choice == '5':
                    print("Voice Assistant is active. Please say your command.")
                    speak_text("Please say the number for the command you want to perform: 1 for summarize, 2 for translate, 3 for expand, 4 for fact-check.")
                    record_audio(WAVE_OUTPUT_FILENAME)
                    command = recognize_speech(WAVE_OUTPUT_FILENAME)
                    if command:
                        print(f"Processing command: {command}")
                        command_number = get_command_number(command)
                        switch_voice_assistant(command_number, f)
                    else:
                        speak_text("I didn't catch that. Please try again.")
                    f.write("\n" + "="*50 + "\n\n")
                elif choice == '6':
                    break
                else:
                    print("Invalid choice. Please try again.")
            except EOFError:
                print("Input stream terminated. Exiting...")
                break

def read_multiline_input():
    lines = []
    paragraph = []
    while True:
        line = input()
        if line == "\n":
            if paragraph:
                lines.append("\n".join(paragraph))
                paragraph = []
            else:
                break
        else:
            paragraph.append(line)
    if paragraph:
        lines.append("\n".join(paragraph))
    return "\n\n".join(lines)

def summarization_menu(text, summarization_choice, file_handle):
    try:
        if summarization_choice == "1":
            paragraphs = text.split("\n\n")
            summaries = [summarize_text(paragraph, summarization_type="each_paragraph") for paragraph in paragraphs]
            file_handle.write("\nSummaries of each paragraph:\n")
            for i, summary in enumerate(summaries):
                file_handle.write(f"Paragraph {i+1} Summary:\n{summary}\n")
                print(f"Paragraph {i+1} Summary:\n{summary}\n")
            file_handle.flush() 
        elif summarization_choice == "2":
            summary = summarize_text(text, summarization_type="whole_text")
            file_handle.write("\nSummary of the entire text:\n")
            file_handle.write(f"{summary}\n")
            print("\nSummary of the entire text:\n")
            print(summary)
            file_handle.flush()  
        else:
            print("Invalid choice. Exiting.")
    except requests.exceptions.ConnectionError as e:
        print(f"Failed to summarize text due to a connection error: {e}")
    except Exception as e:
        print(f"An error occurred while summarizing text: {e}")

def get_command_number(command):
    command = command.strip().lower()
    if "1" in command or "one" in command:
        return 1
    elif "2" in command or "two" in command:
        return 2
    elif "3" in command or "three" in command:
        return 3
    elif "4" in command or "four" in command:
        return 4
    else:
        return None

def switch_voice_assistant(command_number, file_handle):
    if command_number == 1:
        speak_text("Please say the text you want to summarize.")
        record_audio(WAVE_OUTPUT_FILENAME)
        text = recognize_speech(WAVE_OUTPUT_FILENAME)
        if text:
            summarization_menu(text, "2", file_handle)
    elif command_number == 2:
        speak_text("Please say the text you want to translate.")
        record_audio(WAVE_OUTPUT_FILENAME)
        text = recognize_speech(WAVE_OUTPUT_FILENAME)
        if text:
            speak_text("Please say the target language.")
            record_audio(WAVE_OUTPUT_FILENAME)
            target_language = recognize_speech(WAVE_OUTPUT_FILENAME)
            if target_language:
                translated_text = handle_translation(text, "en_XX", target_language, file_handle)
                speak_text("Translation completed. Here is the translation.")
                speak_text(translated_text)
    elif command_number == 3:
        speak_text("Please say the prompt you want to expand.")
        record_audio(WAVE_OUTPUT_FILENAME)
        prompt = recognize_speech(WAVE_OUTPUT_FILENAME)
        if prompt:
            expanded_text = handle_expansion(prompt, file_handle)
            speak_text("Expansion completed. Here is the expanded text.")
            speak_text(expanded_text)
    elif command_number == 4:
        speak_text("Please say the text you want to fact-check or ask.")
        record_audio(WAVE_OUTPUT_FILENAME)
        prompt = recognize_speech(WAVE_OUTPUT_FILENAME)
        if prompt:
            fact_checked_text = handle_fact_check(prompt, file_handle)
            speak_text("Fact-checking completed. Here is the result.")
            speak_text(fact_checked_text)
    else:
        speak_text("Sorry, I don't understand that command.")

if __name__ == "__main__":
    main()
