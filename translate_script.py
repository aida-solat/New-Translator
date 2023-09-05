from googletrans import Translator

def translate_text(input_text, dest_language='all', src_language='auto'):
    translator = Translator()
    translated = translator.translate(input_text, src=src_language, dest=dest_language)
    input_words = input_text.split()
    translated_words = []
    for word in input_words:
        translated_word = translator.translate(word, src=src_language, dest=dest_language)
        translated_words.append(translated_word.text)
    if dest_language == 'all':
        supported_languages = [lang for lang in googletrans.LANGUAGES]
        translations = []
        for lang in supported_languages:
            translated_word_list = []
            for word in translated_words:
                translated_word = translator.translate(word, src=src_language, dest=lang)
                translated_word_list.append({lang: translated_word.text})
            translations.append(translated_word_list)
        return translations
        supported_languages = [lang for lang in googletrans.LANGUAGES]
        translations = []
        for lang in supported_languages:
            translated = translator.translate(input_text, src=src_language, dest=lang)
            translations.append({lang: translated.text})
        return translations
    else:
        return translated_words

if __name__ == '__main__':
    text = input('Enter the text to translate: ')
    dest_language = input('Enter the desired language (use the language abbreviation, e.g., "en" for English or "all" for all languages): ')
    translated_text = translate_text(text, dest_language=dest_language)
    if isinstance(translated_text, list):
        print('Translations for all languages:')
        for translation in translated_text:
            print(translation)
    else:
        print(f'Translated text: {translated_text}')


