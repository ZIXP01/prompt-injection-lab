# Prompt Injection Lab

A small Python project exploring prompt injection and basic tool authorization

## What it does
- Simulates a vulnerable agent and a defended agent
- Uses a tool authorization gateway to restrict tool access
- Tests benign requests and simulated prompt injection attempts
- Compares baseline and defended results using CSV reports

## Run
```bash
python agent_testing.py
python agent_defended.py
python security_evaluation.py
python compare_results.py
```

## Results
In the current test cases, the baseline triggered the restricted tool in 2 out of 2 simulated attack cases, while the defended version triggered it in 0 out of 2

## Limitations
This is a rule-based educational prototype, not a real LLM agent or a comprehensive security evaluation
