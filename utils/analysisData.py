import yaml, os


class AnalysisData:
    @classmethod
    def get_yml_data(cls, file_name):
        """读取yaml文件数据"""
        # 读
        with open("./data" + os.sep + file_name, "r") as f:
            # 加载
            return yaml.safe_load(f)
