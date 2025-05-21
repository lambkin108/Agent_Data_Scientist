# Data Scientist Agent
Our data scientist agent has three function: visualize data, complete machine learning project and solve simple math problems.

## setup environment
```bash
pip install --upgrade metagpt
cd MetaGPT
metagpt --init-config
```
## setop model api key
```bash
vim ~/.metagpt/config2.yaml
```
find something like 
```bash
llm:
  api_type: "openai"  # or azure / ollama / groq etc. Check LLMType for more options
  model: "gpt-4-turbo"  # or gpt-3.5-turbo
  base_url: "https://api.openai.com/v1"  # or forward url / other llm url
  api_key: "YOUR_API_KEY"
```
change the api_key into your own

## let's start 
Ensure working directory is root of the repository.

for data visualization:
```bash
python data_visualization.py 'your own requirement'
```
for machine learning task:
```bash
python machine_learning.py 'your own requirement'
```
for solve math problems:
```bash
python solve_math_problems.py 'your own requirement'
```