# coding = utf-8
import os
import csv
import json
"""
func options: get, set, once
*note: once -> get once
"""

MODEL = "Huawei_SmartLogger"
SCOPES: dict = {
	"getActiveAdj1": 1,
	"setActiveAdj1": 0,
	"getActiveAdj2": 1,
	"setActiveAdj2": 0,
	"getReactiveAdj1": 1,
	"setReactiveAdj1": 0,
	"getReactiveAdj2": 1,
	"setReactiveAdj2": 0,
	"getActivePowerAdjPercentage": 1,
	"setActivePowerAdjPercentage": 0,
	"getPowerFactorAdj": 1,
	"setPowerFactorAdj": 0,
	"maxReactiveAdj": 1,
	"minReactiveAdj": 1,
	"maxActiveAdj": 1,
	"minActiveAdj": 1,
	"acChargeableElectricEnergy": 1,
	"acDischargeableElectricEnergy": 1,
	"ratedElectricEnergy": 1,
	"maxChargingElectricEnergy": 1,
	"maxDischargingElectricEnergy": 1,
	"storedElectricityPercent": 2,
	"instanceElectricity": 2,
	"powerFactor": 1,
	"generatedElectricity": 2,
	"generatedElectricityToday": 1,
	"acCurrentOfPhaseR": 1,
	"acCurrentOfPhaseS": 1,
	"acCurrentOfPhaseT": 1,
	"activePowerControlMode": 1,
	"targetValueOfActivePowerAdjustment": 1,
	"connectionStatus": 1,
	"alarm1": 1,
	"alarm2": 1,
	"alarm3": 1,
	"alarm4": 1
}

testplan_path: str = os.path.join(os.getcwd(), 'testcases.json')
list_testcases: list = []
csv_title_list: list = ["Product", "Category", "Summary", "Text"]


def execute(scope: dict):
    list_testcases.append(csv_title_list)
    
    with open(testplan_path, encoding="utf-8") as file:
        testplan = file.read()
    file.close()
    testplan: dict = json.loads(testplan)
    
    for i in range(len(testplan["default"])):
        list_testcases.append(
            [
                testplan["project"],testplan["default"][i]["category"],
                testplan["default"][i]["title"].format(model=MODEL),testplan["default"][i]["content"]
            ]
        )
         
    for key, value in SCOPES.items():
        for i in range(len(testplan["general"])):
            list_testcases.append(
                [
                    testplan["project"],testplan["general"][i]["category"],
                    testplan["general"][i]["title"].format(model=MODEL, key=key),testplan["general"][i]["content"]
                ]
            )
        if value == 2:
            for i in range(len(testplan["get"])):
                list_testcases.append(
                    [
                        testplan["project"],testplan["get"][i]["category"],
                        testplan["get"][i]["title"].format(model=MODEL, key=key),testplan["get"][i]["content"].format(model=MODEL)
                     ]
                )
        elif value == 1:
            for i in range(len(testplan["get_once"])):
                list_testcases.append(
                    [
                        testplan["project"],testplan["get_once"][i]["category"],
                        testplan["get_once"][i]["title"].format(model=MODEL, key=key),testplan["get_once"][i]["content"].format(model=MODEL)
                     ]
                )
        elif value == 0:
            for i in range(len(testplan["set"])):
                list_testcases.append(
                    [
                        testplan["project"],testplan["set"][i]["category"],
                        testplan["set"][i]["title"].format(model=MODEL, key=key),testplan["set"][i]["content"].format(model=MODEL)
                     ]
                )

    for i in range(len(testplan["webhook"])):
         list_testcases.append(
            [
                testplan["project"],testplan["webhook"][i]["category"],
                testplan["webhook"][i]["title"].format(model=MODEL),testplan["webhook"][i]["content"]
            ]
        )

    return list_testcases

def create_csv(testcase: list):
    with open(f"testcases/TC_{MODEL}.csv", 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for tc in testcase:
            writer.writerow(tc)


if __name__ == '__main__':
    result = execute(SCOPES)
    create_csv(result)
    # print(testplan_path)
    # print(result)
