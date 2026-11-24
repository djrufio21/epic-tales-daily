"""How the Short narrator says Indian and Sanskrit words.

Each word maps to IPA sounds, written the way the word is said in India
(Sanskrit form, final "a" kept, as on screen). The narrator speaks these
sounds directly instead of guessing from English spelling.

Sound guide for adding words:
  ʌ  short a (as in "but")      aː long aa       ə  light a
  ɪ  short i     iː long ee     ʊ  short u       uː long oo
  eː long e      oː long o      ɛː ai            ɔː au
  t d  soft (teeth) t and d     ʈ ɖ  hard (tongue curled) t and d
  ɳ  hard n      ʂ  hard sh     ɾ  tapped r      ʋ  Indian v/w
  ʰ  after a sound adds breath: tʰ th, dʰ dh, bʰ bh, ɡʰ gh, ʈʰ hard th
  ʧ  ch          ʤ  j           ˈ  goes before the stressed part

New names: add them here when an episode introduces them (see CLAUDE.md).
"""
import re

IPA = {
    # Books and places
    "Ramayana": "ɾaːmˈaːjəɳə", "Mahabharata": "məhaːbʰˈaːɾətə", "Sanskrit": "sˈʌnskɾɪt",
    "Ayodhya": "əjˈoːdʰjaː", "Sarayu": "sˈʌɾəjuː", "Mithila": "mˈɪtʰɪlaː", "Ganga": "ɡˈʌŋɡaː",
    "Himalaya": "hɪmˈaːləjə", "Vishala": "ʋɪʃˈaːlaː", "Siddhashrama": "sˈɪddʰaːʃɾəmə",
    "Bhagirathi": "bʰəɡˈiːɾətʰiː", "Kanda": "kˈaːɳɖə", "Lanka": "lˈʌŋkaː",
    # Royal family
    "Dasharatha": "dˈʌʃəɾətʰə", "Kausalya": "kˈɔːsəljaː", "Kaikeyi": "kˈɛːkeːjiː",
    "Sumitra": "sʊmˈɪtɾaː", "Rama": "ɾˈaːmə", "Lakshmana": "lˈʌkʃməɳə", "Bharata": "bʰˈʌɾətə",
    "Shatrughna": "ʃətɾˈʊɡʰnə", "Sita": "sˈiːtaː", "Janaka": "ʤˈʌnəkə", "Urmila": "ˈʊɾmɪlaː",
    "Mandavi": "mˈaːɳɖəʋiː", "Shrutakirti": "ʃɾʊtəkˈiːɾtiː", "Kushadhvaja": "kʊʃədʰʋˈʌʤə",
    # Sages and teachers
    "Vasishtha": "ʋəsˈɪʂʈʰə", "Vishvamitra": "ʋɪʃʋaːmˈɪtɾə", "Gautama": "ɡˈɔːtəmə",
    "Ahalya": "əhˈʌljaː", "Shatananda": "ʃətaːnˈʌndə", "Kapila": "kˈʌpɪlə",
    "Valmiki": "ʋaːlmˈiːkiː", "Vyasa": "ʋjˈaːsə", "Parashurama": "pəɾəʃʊɾˈaːmə",
    "Vamadeva": "ʋaːmədˈeːʋə",
    # Kings of old
    "Sagara": "sˈʌɡəɾə", "Bhagiratha": "bʰəɡˈiːɾətʰə", "Devarata": "deːʋəɾˈaːtə",
    # Gods and divine beings
    "Shiva": "ʃˈɪʋə", "Vishnu": "ʋˈɪʂɳʊ", "Brahma": "bɾˈʌhmaː", "Indra": "ˈɪndɾə",
    "Vamana": "ʋˈaːmənə", "Hanuman": "hˈʌnʊmaːn", "Pinaka": "pɪnˈaːkə",
    # Demons
    "Tataka": "tˈaːʈəkaː", "Maricha": "maːɾˈiːʧə", "Subahu": "sʊbˈaːhʊ", "Ravana": "ɾˈaːʋəɳə",
    # Mantras and weapons
    "Bala": "bˈʌlaː", "Atibala": "ˈʌtɪbəlaː", "Manava": "mˈaːnəʋə",
    "Atithi": "ˈʌtɪtʰɪ", "Devo": "dˈeːʋoː", "Bhava": "bʰˈʌʋə",
    # Values
    "Shraddha": "ʃɾˈʌddʰaː", "Vinaya": "ʋˈɪnəjə", "Satya": "sˈʌtjə", "Dharma": "dʰˈʌɾmə",
    "Kritajnata": "kɾɪtˈʌɡjətaː", "Kartavya": "kˈʌɾtəʋjə", "Shravana": "ʃɾˈʌʋəɳə",
    "Karuna": "kˈʌɾʊɳaː", "Dhairya": "dʰˈɛːɾjə", "Mangala": "mˈʌŋɡələ", "Kutumba": "kʊʈˈʊmbə",
    "Shanti": "ʃˈaːntiː", "Seva": "sˈeːʋaː", "Kshama": "kʃˈʌmaː",
    # Everyday words
    "Vedas": "ʋˈeːdəz", "guru": "ɡˈʊɾʊ", "gurus": "ɡˈʊɾʊz", "ashram": "ˈaːʃɾəm",
    "astra": "ˈʌstɾə", "astras": "ˈʌstɾəz", "deva": "dˈeːʋə", "devas": "dˈeːʋəz",
    "mantra": "mˈʌntɾə", "mantras": "mˈʌntɾəz", "rakshasa": "ɾˈaːkʃəsə",
    "rakshasas": "ɾˈaːkʃəsəz", "rakshasi": "ɾˈaːkʃəsiː", "rishi": "ɾˈɪʃiː",
    "rishis": "ɾˈɪʃiːz", "tapas": "tˈʌpəs", "yajna": "jˈʌɡjə", "puja": "pˈuːʤaː",
}
# Lower case forms (dharma, seva, shraddha...) say the same as capitalised ones.
IPA.update({k.lower(): v for k, v in list(IPA.items()) if k.lower() not in IPA})

_WORD = re.compile(r"\b(" + "|".join(sorted(map(re.escape, IPA), key=len, reverse=True))
                   + r")(['’]s)?\b")


def to_phonemes(text, english):
    """Turn text into narrator sounds. `english(str)` phonemizes plain English."""
    out, pos = [], 0
    for m in _WORD.finditer(text):
        if text[pos:m.start()].strip():
            out.append(english(text[pos:m.start()]))
        out.append(IPA[m.group(1)] + ("z" if m.group(2) else ""))
        pos = m.end()
    if text[pos:].strip():
        out.append(english(text[pos:]))
    # Punctuation right after a name is kept by the English piece that follows.
    return re.sub(r"\s+([,.;:!?])", r"\1", " ".join(p.strip() for p in out if p.strip()))
