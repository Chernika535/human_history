# Build-time only. Provide an extracted Argos ru_en 1.9 model; no translation service runs in the site.
import pathlib,json,sys,re
import ctranslate2,sentencepiece as sp
root=pathlib.Path(__file__).resolve().parents[1];model=pathlib.Path(sys.argv[1]);source=json.loads((root/'dist/locales/ru-source.json').read_text());out=root/'dist/locales/en.json';values=json.loads(out.read_text()) if out.exists() else {}
processor=sp.SentencePieceProcessor(model_file=str(model/'sentencepiece.model'));translator=ctranslate2.Translator(str(model/'model'),device='cpu',compute_type='int8',inter_threads=2,intra_threads=3)
missing=[s for s in source if s not in values]
for i in range(0,len(missing),32):
 batch=missing[i:i+32];encoded=[processor.encode(s,out_type=str) for s in batch];result=translator.translate_batch(encoded,beam_size=2,max_batch_size=16,max_decoding_length=512)
 for text,r in zip(batch,result):values[text]=processor.decode(r.hypotheses[0])
 out.write_text(json.dumps(values,ensure_ascii=False,indent=1)+'\n');print(i+len(batch),'/',len(missing),flush=True)
