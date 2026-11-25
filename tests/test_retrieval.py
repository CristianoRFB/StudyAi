import unittest
from app import buscar, prompt
class RetrievalTests(unittest.TestCase):
 def test_index_has_documents(self): self.assertTrue(buscar('Quais os requisitos do projeto?'))
 def test_missing_terms(self): self.assertEqual(buscar('zzqxwvzzq'), [])
 def test_prompt_has_citations(self): self.assertIn('FONTES:',prompt('Qual a data da apresentação?',buscar('Qual a data da apresentação?')))
