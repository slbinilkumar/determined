import boto3
import datetime
import os

from dateutil.tz import tzutc


def check_conditions(stack: dict, target_stacks: dict, time_diff: datetime.timedelta):
    current_time = datetime.datetime.now(tz=tzutc())

    for k in target_stacks:
        if k in stack['StackName'] and current_time-stack['CreationTime'] > time_diff:
            target_stacks[k].append(stack['StackName'])


if __name__ == "__main__":
    println("HELLO!")
    
    client = boto3.client('cloudformation')

    difference = datetime.timedelta(seconds=6)
    response = client.describe_stacks()

    # targetStacks = {'nightly-':[], 'e2e-gpu-':[], 'parallel-':[]}
    targets = {'eliu-test2':[]}

    for each in response['Stacks']:
        check_conditions(each, targets, difference)

    for k, lists in targets.items():
        for each in lists:
            print(each)
            print("det-deploy aws down --cluster-id " + each)
            # os.system("det-deploy aws down --cluster-id " + each)
