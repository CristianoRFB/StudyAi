from bs4 import BeautifulSoup
from pathlib import Path
import json
p=Path(__file__).parent
s=BeautifulSoup((p/'guia.html').read_text(),'html.parser')
docs=[]
for sec in s.select('section[id]'):
 for i,el in enumerate(sec.select('tr, .requisito, .tema-card, .faq-item, .timeline-item, .destaque, .destaque-verde, .destaque-vermelho, .destaque-azul, li')):
  if el.find_parent(['li','tr']) or el.find_parent(class_=['requisito','tema-card','faq-item','destaque','destaque-verde','destaque-vermelho','destaque-azul']): continue
  t=' '.join(el.stripped_strings)
  if len(t)>35: docs.append({'id':f'{sec["id"]}-{i+1}','texto':t})
(p/'base.json').write_text(json.dumps(docs,ensure_ascii=False,indent=2))
