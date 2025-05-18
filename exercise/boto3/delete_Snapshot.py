import boto3
from botocore.config import Config
import botocore


my_config = Config(
    region_name = 'us-east-2',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)
ec2 = boto3.client('ec2', config=my_config)

response = ec2.describe_snapshots(OwnerIds=['self'])

print(response)

for snapshot in response['Snapshots']:
    volume_id = snapshot.get('VolumeId')
    snapshot_id = snapshot.get('SnapshotId')

    if not volume_id:
        ec2.delete_snapshot(SnapshotId=snapshot_id)
        print(f"EBS snapshot {snapshot_id} deleted, it is not attached to any volme")
    else:
        try:
          volume_data = ec2.describe_volumes(VolumeIds=[volume_id])
          if not volume_data['Volumes'] [0] ['Attachments']:
              ec2.delete_snapshot(SnapshotId=snapshot_id)
              print(f"Volume was not attached to any instance, so deleting snapshot {snapshot_id} ot was takem from a volume {volume_id}")
        except ec2.exceptions.ClientError as e:
            if e.response['Error']['Code'] == "InvalidVolume.NotFound":
                botocore.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")