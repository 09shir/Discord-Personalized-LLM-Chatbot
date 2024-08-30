from sagemaker.s3 import S3Uploader
import sagemaker

output_bucket = sagemaker.Session().default_bucket()
dataset_file = "~/documents/dataset.jsonl"
template_file = "~/documents/template.jsonl"
train_data_location = f"s3://{output_bucket}/training_data"
S3Uploader.upload(dataset_file, train_data_location)
S3Uploader.upload(template_file, train_data_location)
print(f"Training data: {train_data_location}")