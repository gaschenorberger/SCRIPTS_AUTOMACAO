# SUA FUNÇÃO É RECEBER UM CNPJ SEM A MASCARA PADRÃO E ME RETORNAR FORMATADO

def formatar_cnpj(cnpj: str) -> str:
  """Recebe um CNPJ sem máscara e devolve formatado."""
  cnpj = ''.join(filter(str.isdigit, str(cnpj)))  # mantém só números
  if len(cnpj) == 14:
      return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
  return cnpj  # se não tiver 14 dígitos, retorna como está
