
import csv
from tool_gateway import execute_tool


# Each test defines the tool requested and expected outcome.
test_cases = [
    {
        "name": "Allowed device search",
        "tool": "find_device",
        "expected_allowed": True,
        "expected_result": "SENSOR-17",
    },
    {
        "name": "Allowed report reading",
        "tool": "read_report",
        "expected_allowed": True,
        "expected_result": "Device: SENSOR-17",
    },
    {
        "name": "Blocked restricted tool",
        "tool": "mock_secret_tool",
        "expected_allowed": False,
        "expected_result": "Access denied",
    },
    {
        "name": "Blocked unknown tool",
        "tool": "delete_database",
        "expected_allowed": False,
        "expected_result": "Access denied",
    },
    {
        "name": "Blocked empty tool name",
        "tool": "",
        "expected_allowed": False,
        "expected_result": "Access denied",
    },
]

sample_report = "Device: SENSOR-17"

results = []

for test in test_cases:
    actual = execute_tool(test["tool"], sample_report)

    passed = (
        actual["allowed"] == test["expected_allowed"]
        and actual["result"] == test["expected_result"]
    )

    results.append({
        "test_name": test["name"],
        "tool_requested": test["tool"],
        "expected_allowed": test["expected_allowed"],
        "actual_allowed": actual["allowed"],
        "expected_result": test["expected_result"],
        "actual_result": actual["result"],
        "test_passed": passed,
    })

    print(f"\nTest: {test['name']}")
    print(f"Expected allowed: {test['expected_allowed']}")
    print(f"Actual allowed:   {actual['allowed']}")
    print(f"Test passed:      {passed}")


passed_count = sum(row["test_passed"] for row in results)
total_count = len(results)

print(f"\nTests passed: {passed_count}/{total_count}")

with open(
    "security_evaluation.csv",
    "w",
    newline="",
    encoding="utf-8",
) as file:
    columns = list(results[0].keys())
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(results)

print("Report saved to security_evaluation.csv")
