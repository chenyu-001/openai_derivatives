import openai

# 确保你设置了 API 密钥
openai.api_key = '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'

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Translate the following English text to French: '{}'",
  max_tokens=60
)

print(response.choices[0].text.strip())
