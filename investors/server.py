# Import dependencies
from mcp.server.fastmcp import FastMCP
import json
import requests
from typing import List


# Server created
mcp = FastMCP('')

# Create the tool
@mcp.tool()
def PredictChurn(data:List[dict]) -> str:
	"""This tool predicts whether an employee will churn or not,
	Args:
		data: employee atributes which are used for inference. Example payload

		[{
			'YearAtCompany':10,
			'EmployeeSatisfaction':0.99,
			'Position':'Non-Manager',
			'Salary':5.0
		}]

	Returns:
		str: 1=churn or 0 = no churn"""

	payload = data[0]
	response = requests.post("http://127.0.0.1:8000", headers={"Accept":"application/json", "Content-Type":"application/json"}, data=json.dumps(payload),
	)

	return response.json()

if __name__ == '__main__':
	mcp.run(transport="stdio")