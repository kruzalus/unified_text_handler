import spacy
import time
import html

nlp1 = spacy.load("en_core_web_sm")
nlp2 = spacy.load("ru_core_news_sm")


class Service:
	def __init__(self):
		self.nlp1 = nlp1
		self.nlp2 = nlp2

	def get_shortened_text(self, text):
		print("inside get_shortened_text")
		print(text)
		result = html.escape(text)
		prev_step_text = ''

		while result != prev_step_text:
			prev_step_text = result
			print("////\\\\")
			print(result)
			result = result.replace("  ", " ")
			result = result.replace("🇷🇺🇷🇺", "🇷🇺")
			result = result.replace("🇺🇸🇺🇸", "🇺🇸")
			result = result.replace("🇪🇺🇪🇺", "🇪🇺")
		# if IS_NEED_REPLACE_EMOJI:
		# 	return regrex_pattern.sub(r'', result)
		return result

	async def get_handled_text(self, text, language_pack):
		time_start = time.time()
		lowered_shortened = self.get_shortened_text(text).lower()
		print("TIME TO SHORTEN: " + str(time.time() - time_start))
		if language_pack == 'ru_core_news_sm':
			time_start = time.time()
			doc = self.nlp2(lowered_shortened)
			print("TIME TO RU: " + str(time.time() - time_start))
		else:
			time_start = time.time()
			doc = self.nlp1(lowered_shortened)
			print("TIME TO EM: " + str(time.time() - time_start))

		time_start = time.time()
		result = ''.join(
			[(token.lemma_ + (token.whitespace_ if token.whitespace_ else '')) for sent in doc.sents for token in sent])
		print("TIME TO HANDLE: " + str(time.time() - time_start))
		return result

	async def get_text(self, text):
		lemmanized_text_en = await self.get_handled_text(text, 'en_core_web_sm')
		lemmanized_text_ru = await self.get_handled_text(lemmanized_text_en, 'ru_core_news_sm')

		return {"result": lemmanized_text_ru}
