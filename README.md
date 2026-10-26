# Uncensored LLM API for developers in India — OpenAI-compatible

> OpenAI-compatible API for teams shipping from India. Hinglish-friendly, respects your system prompt, no warning paragraph bolted onto every reply. Base: https://uncensored-llm.sbs/v1

**API:** https://uncensored-llm.sbs/v1
**Site:** https://uncensored-llm.sbs

If you have used a language model to write about politics, health, offensive security or any topic a foreign provider considers sensitive, you know the result: a generic refusal, a safety notice where the content should be, half an answer. This page describes a direct alternative — an OpenAI-compatible API that answers the question that was asked.

## Why this matters for teams building in India

Indian products rarely ship in a single register. A support bot has to handle English, Hindi and the code-mixed middle that people actually type, and it has to do that without a policy paragraph at the start of every message. The second friction point is cost and control: you want streaming, tool calling and JSON mode on the same SDK you already use, with the scope decided by your product team. That is what this endpoint gives you, and the only hard line kept is illegal content.

## Example call

```bash
export UNLLM_KEY="sk-..."
curl https://uncensored-llm.sbs/v1/chat/completions \
  -H "Authorization: Bearer $UNLLM_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"uncensored-llm","messages":[{"role":"user","content":"Explain in plain terms how crypto market cap is calculated."}],"stream":true}'
```

```python
# pip install openai
from openai import OpenAI
client = OpenAI(base_url="https://uncensored-llm.sbs/v1", api_key="sk-...")
r = client.chat.completions.create(
    model="uncensored-llm",
    messages=[{"role": "user", "content": "Explain in plain terms how crypto market cap is calculated."}],
)
print(r.choices[0].message.content)
```

```javascript
import OpenAI from "openai";
const ai = new OpenAI({ baseURL: "https://uncensored-llm.sbs/v1", apiKey: process.env.UNLLM_KEY });
const r = await ai.chat.completions.create({ model: "uncensored-llm", messages: [{ role: "user", content: "Explain in plain terms how crypto market cap is calculated." }] });
console.log(r.choices[0].message.content);
```

## Where it is actually used

| Case | Why |
|---|---|
| Support across languages | One bot for English, Hindi and code-mixed users. |
| Product content | Listings, scripts and emails without translated tone. |
| Authorised security testing | Offensive work under a signed scope from the client. |
| Adult fiction (18+) | Explicit scenes between adults, no fade to black. |

## Latency from your city

Latency is your ISP's business, not your passport. Measure from your own machine first:

```bash
curl -o /dev/null -s -w '%{time_total}s\n' https://uncensored-llm.sbs/v1/models
```

| City | State |
|---|---|
| Mumbai | Maharashtra |
| Delhi NCR | Delhi |
| Bengaluru | Karnataka |
| Hyderabad | Telangana |
| Chennai | Tamil Nadu |
| Pune | Maharashtra |
| Ahmedabad | Gujarat |
| Kolkata | West Bengal |
| Jaipur | Rajasthan |
| Kochi | Kerala |
| Indore | Madhya Pradesh |
| Chandigarh | Punjab |

## Questions that actually come up

### Is it really OpenAI-compatible?

Yes. /v1/chat/completions, /v1/models and SSE streaming use the same event format. The official SDK works by changing base_url alone.

### Is there a free tier or trial?

Current terms are published at https://uncensored-llm.sbs. Price changes are announced there, not in this repository.

### What gets blocked?

Illegal content, including any material involving minors. Outside that, the answer is about the request.

### Will it work with Open WebUI or LibreChat?

Yes, both accept an OpenAI-compatible base URL. Enter https://uncensored-llm.sbs/v1 and your key.

### How do I keep the key safe?

Environment variable per environment, rotate periodically, never in the frontend or a public repo. If you are on a shared dev box, use a vault.

## This documentation in other languages

- [pt-BR] https://brown1023.github.io/llm-api-sem-censura-brasil/
- [es-419] https://brown1023.github.io/api-llm-sin-censura-latam/
- [id-ID] https://ryuuless.github.io/uncensored-llm-api-indonesia/
- [vi-VN] https://ryuuless.github.io/uncensored-llm-api-vietnam/
- [tr-TR] https://askcode24.github.io/sansursuz-llm-api-turkiye/
- [de-DE] https://askcode24.github.io/uncensored-llm-api-deutschland/
- [es-ES] https://palazuel0s2004.github.io/api-llm-sin-censura-espana/
- [it-IT] https://palazuel0s2004.github.io/llm-api-senza-censura-italia/
- [en-PH] https://nirav0712.github.io/uncensored-llm-api-philippines/
- [ar] https://mohamedabderrehman.github.io/uncensored-llm-api-arabia/
- [ar-EG] https://mohamedabderrehman.github.io/uncensored-llm-api-egypt/

---

uncensored-llm.sbs — OpenAI-compatible API. Illegal content, including any material involving minors, is blocked. Everything else is the caller's responsibility.