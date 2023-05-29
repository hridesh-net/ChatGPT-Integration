
# ChatGPT Using simple Requets Model

This app is to give an overview of how to access Openai Models using simple python code for any purpose.

- This repository contains several method to do this.
- Also in this repository you'll find integration of several different Openai Models.

you can understand the request parameters and send create your own requesrests or you can Directly copy bellow commands and run them in there particular environment.
## API Reference
Endpoint: https://api.openai.com

### Get all Models

```http
  GET /v1/models
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `string` | **Required**. Your API key |

on Bash/shell
```shell
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

In python
```python
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()
```

### Model Retrival

```http
  GET v1/models/{model}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `string` | **Required**. Your API key |
| `model` | `string` | **Required**. Model you want to retrive |

In shell/bash
```shell
curl https://api.openai.com/v1/models/text-davinci-003 \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

In Python
```python
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.retrieve("text-davinci-003")
```

### Chat Completeion (ChatGPT-3)

```http
  POST v1/chat/completions
```
**Inside Header**
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Content-Type`  | `string` | **Required**. application/json |
| `Authorization` | `string` | **Required**. Your API key | 

**Inside Body**
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `model`  | `string` | **Required**. Model you are using ("gpt-3.5-turbo") |
| `messages` | `string` | **Required**. Need to pass message to GPT with the role in array -> [{"role": "user", "content": "Hello!"}]| 

In shell/Bash
```shell
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

In python
```python
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)

```


