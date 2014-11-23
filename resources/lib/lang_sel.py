import xbmc
import xbmcgui
import xbmcaddon

__addon__        = xbmcaddon.Addon('service.native.tongue')
__addonid__      = __addon__.getAddonInfo('id')
__setting__      = __addon__.getSetting
script_path      = __addon__.getAddonInfo('path')
addon_path       = xbmc.translatePath('special://home/addons')
__setting__      = __addon__.setSetting


ACTION_PREVIOUS_MENU = 10
ACTION_NAV_BACK      = 92
CLOSE                 = 5
HEADING              = 1
ACTION_SELECT_ITEM   = 7

language = {'Abkhazian (abk)' : 'abk',
	'Afar (aar)' : 'aar',
	'Afrikaans (afr)' : 'afr',
	'Albanian (alb)' : 'alb',
	'Albanian (sqi)' : 'sqi',
	'Amharic (amh)' : 'amh',
	'Arabic (ara)' : 'ara',
	'Aragonese (arg)' : 'arg',
	'Armenian (arm)' : 'arm',
	'Armenian (hye)' : 'hye',
	'Assamese (asm)' : 'asm',
	'Avestan (ave)' : 'ave',
	'Aymara (aym)' : 'aym',
	'Azerbaijani (aze)' : 'aze',
	'Bashkir (bak)' : 'bak',
	'Basque (baq)' : 'baq',
	'Basque (eus)' : 'eus',
	'Belarusian (bel)' : 'bel',
	'Bengali (ben)' : 'ben',
	'Bihari (bih)' : 'bih',
	'Bislama (bis)' : 'bis',
	'Bosnian (bos)' : 'bos',
	'Breton (bre)' : 'bre',
	'Bulgarian (bul)' : 'bul',
	'Burmese (bur)' : 'bur',
	'Burmese (mya)' : 'mya',
	'Catalan (cat)' : 'cat',
	'Chamorro (cha)' : 'cha',
	'Chechen (che)' : 'che',
	'Chinese (chi)' : 'chi',
	'Chinese (zho)' : 'zho',
	'Church Slavic; Slavonic; Old Bulgarian (chu)' : 'chu',
	'Chuvash (chv)' : 'chv',
	'Cornish (cor)' : 'cor',
	'Corsican (cos)' : 'cos',
	'Croatian (hrv)' : 'hrv',
	'Croatian (scr)' : 'scr',
	'Czech (ces)' : 'ces',
	'Czech (cze)' : 'cze',
	'Danish (dan)' : 'dan',
	'Divehi; Dhivehi; Maldivian (div)' : 'div',
	'Dutch (dut)' : 'dut',
	'Dutch (nld)' : 'nld',
	'Dzongkha (dzo)' : 'dzo',
	'English (eng)' : 'eng',
	'Esperanto (epo)' : 'epo',
	'Estonian (est)' : 'est',
	'Faroese (fao)' : 'fao',
	'Fijian (fij)' : 'fij',
	'Finnish (fin)' : 'fin',
	'French (fra)' : 'fra',
	'French (fre)' : 'fre',
	'Gaelic; Scottish Gaelic (gla)' : 'gla',
	'Galician (glg)' : 'glg',
	'Georgian (geo)' : 'geo',
	'Georgian (kat)' : 'kat',
	'German (deu)' : 'deu',
	'German (ger)' : 'ger',
	'Greek, Modern (1453-) (ell)' : 'ell',
	'Greek, Modern (1453-) (gre)' : 'gre',
	'Guarani (grn)' : 'grn',
	'Gujarati (guj)' : 'guj',
	'Haitian; Haitian Creole (hat)' : 'hat',
	'Hausa (hau)' : 'hau',
	'Hebrew (heb)' : 'heb',
	'Herero (her)' : 'her',
	'Hindi (hin)' : 'hin',
	'Hiri Motu (hmo)' : 'hmo',
	'Hungarian (hun)' : 'hun',
	'Icelandic (ice)' : 'ice',
	'Icelandic (isl)' : 'isl',
	'Ido (ido)' : 'ido',
	'Indonesian (ind)' : 'ind',
	'Interlingua (International Auxiliary Language Association) (ina)' : 'ina',
	'Interlingue (ile)' : 'ile',
	'Inuktitut (iku)' : 'iku',
	'Inupiaq (ipk)' : 'ipk',
	'Irish (gle)' : 'gle',
	'Italian (ita)' : 'ita',
	'Japanese (jpn)' : 'jpn',
	'Javanese (jav)' : 'jav',
	'Kalaallisut (kal)' : 'kal',
	'Kannada (kan)' : 'kan',
	'Kashmiri (kas)' : 'kas',
	'Kazakh (kaz)' : 'kaz',
	'Khmer (khm)' : 'khm',
	'Kikuyu; Gikuyu (kik)' : 'kik',
	'Kinyarwanda (kin)' : 'kin',
	'Kirghiz (kir)' : 'kir',
	'Komi (kom)' : 'kom',
	'Korean (kor)' : 'kor',
	'Kuanyama; Kwanyama (kua)' : 'kua',
	'Kurdish (kur)' : 'kur',
	'Lao (lao)' : 'lao',
	'Latin (lat)' : 'lat',
	'Latvian (lav)' : 'lav',
	'Limburgan; Limburger; Limburgish (lim)' : 'lim',
	'Lingala (lin)' : 'lin',
	'Lithuanian (lit)' : 'lit',
	'Luxembourgish; Letzeburgesch (ltz)' : 'ltz',
	'Macedonian (mac)' : 'mac',
	'Macedonian (mkd)' : 'mkd',
	'Malagasy (mlg)' : 'mlg',
	'Malay (may)' : 'may',
	'Malay (msa)' : 'msa',
	'Malayalam (mal)' : 'mal',
	'Maltese (mlt)' : 'mlt',
	'Manx (glv)' : 'glv',
	'Maori (mao)' : 'mao',
	'Maori (mri)' : 'mri',
	'Marathi (mar)' : 'mar',
	'Marshallese (mah)' : 'mah',
	'Moldavian (mol)' : 'mol',
	'Mongolian (mon)' : 'mon',
	'Nauru (nau)' : 'nau',
	'Navaho, Navajo (nav)' : 'nav',
	'Ndebele, North (nde)' : 'nde',
	'Ndebele, South (nbl)' : 'nbl',
	'Ndonga (ndo)' : 'ndo',
	'Nepali (nep)' : 'nep',
	'Northern Sami (sme)' : 'sme',
	'Norwegian (nor)' : 'nor',
	'Norwegian Bokmal (nob)' : 'nob',
	'Norwegian Nynorsk (nno)' : 'nno',
	'Nyanja; Chichewa; Chewa (nya)' : 'nya',
	'Occitan (post 1500); Provencal (oci)' : 'oci',
	'Oriya (ori)' : 'ori',
	'Oromo (orm)' : 'orm',
	'Ossetian; Ossetic (oss)' : 'oss',
	'Pali (pli)' : 'pli',
	'Panjabi (pan)' : 'pan',
	'Persian (fas)' : 'fas',
	'Persian (per)' : 'per',
	'Polish (pol)' : 'pol',
	'Portuguese (por)' : 'por',
	'Pushto (pus)' : 'pus',
	'Quechua (que)' : 'que',
	'Raeto-Romance (roh)' : 'roh',
	'Romanian (ron)' : 'ron',
	'Romanian (rum)' : 'rum',
	'Rundi (run)' : 'run',
	'Russian (rus)' : 'rus',
	'Samoan (smo)' : 'smo',
	'Sango (sag)' : 'sag',
	'Sanskrit (san)' : 'san',
	'Sardinian (srd)' : 'srd',
	'Serbian (scc)' : 'scc',
	'Serbian (srp)' : 'srp',
	'Shona (sna)' : 'sna',
	'Sichuan Yi (iii)' : 'iii',
	'Sindhi (snd)' : 'snd',
	'Sinhala; Sinhalese (sin)' : 'sin',
	'Slovak (slk)' : 'slk',
	'Slovak (slo)' : 'slo',
	'Slovenian (slv)' : 'slv',
	'Somali (som)' : 'som',
	'Sotho, Southern (sot)' : 'sot',
	'Spanish; Castilian (spa)' : 'spa',
	'Sundanese (sun)' : 'sun',
	'Swahili (swa)' : 'swa',
	'Swati (ssw)' : 'ssw',
	'Swedish (swe)' : 'swe',
	'Tagalog (tgl)' : 'tgl',
	'Tahitian (tah)' : 'tah',
	'Tajik (tgk)' : 'tgk',
	'Tamil (tam)' : 'tam',
	'Tatar (tat)' : 'tat',
	'Telugu (tel)' : 'tel',
	'Thai (tha)' : 'tha',
	'Tibetan (bod)' : 'bod',
	'Tibetan (tib)' : 'tib',
	'Tigrinya (tir)' : 'tir',
	'Tonga (Tonga Islands) (ton)' : 'ton',
	'Tsonga (tso)' : 'tso',
	'Tswana (tsn)' : 'tsn',
	'Turkish (tur)' : 'tur',
	'Turkmen (tuk)' : 'tuk',
	'Twi (twi)' : 'twi',
	'Uighur (uig)' : 'uig',
	'Ukrainian (ukr)' : 'ukr',
	'Urdu (urd)' : 'urd',
	'Uzbek (uzb)' : 'uzb',
	'Vietnamese (vie)' : 'vie',
	'Volapuk (vol)' : 'vol',
	'Walloon (wln)' : 'wln',
	'Welsh (cym)' : 'cym',
	'Welsh (wel)' : 'wel',
	'Western Frisian (fry)' : 'fry',
	'Wolof (wol)' : 'wol',
	'Xhosa (xho)' : 'xho',
	'Yiddish (yid)' : 'yid',
	'Yoruba (yor)' : 'yor',
	'Zhuang; Chuang (zha)' : 'zha',
	'Zulu (zul)' : 'zul'}






class xGUI(xbmcgui.WindowXMLDialog):

	def onInit(self):

		global language
		global all_variables

		self.language = language
		self.all_variables = all_variables
		self.all_variables.sort()

		# Save button
		self.ok = self.getControl(CLOSE)
		self.ok.setLabel('Close')

		# Heading
		self.hdg = self.getControl(HEADING)
		self.hdg.setLabel('Choose Language')
		self.hdg.setVisible(True)

		# Hide unused list frame
		self.x = self.getControl(3)
		self.x.setVisible(False)

		# Populate the list frame
		self.name_list      = self.getControl(6)

		# Set action when clicking right from the Save button
		self.ok.controlRight(self.name_list)

		for i in self.all_variables:
			# populate the random list
			self.tmp = xbmcgui.ListItem(i)
			self.name_list.addItem(self.tmp)

		self.setFocus(self.name_list)

	def onAction(self, action):
		actionID = action.getId()
		if (actionID in (ACTION_PREVIOUS_MENU, ACTION_NAV_BACK)):
			self.close()

	def onClick(self, controlID):

		global __setting__

		if controlID == CLOSE:
			
			self.close()

		else:
			item = self.name_list.getSelectedPosition()
			abbreviation = language.get(self.all_variables[item], 'eng')
			__setting__('language_string', abbreviation)
			self.close()

def open_window():

	global all_variables
	global script_path

	all_variables  = language.keys()

	# create and launch the custom window
	creation = xGUI("DialogSelect.xml", script_path, 'Default')
	creation.doModal()

if __name__ == "__main__":
	open_window()