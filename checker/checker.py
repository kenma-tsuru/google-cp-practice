import subprocess
import tempfile
from os.path import join


class Checker:
    def __init__(self, 
                 problem_file_path: str, 
                 submission_file_path: str):
        self.problem_file_path = problem_file_path
        self.submission_file_path = submission_file_path
    
    def run(self):
        try:
            instance = subprocess.run(['python', self.submission_file_path], 
                                      stdin=open(self.problem_file_path, "r"), 
                                      stdout=subprocess.PIPE,
                                      check=True)
            label = open(r"checker\sample_output.txt", "r").read()
            answer = instance.stdout.strip().decode()
            print("answer:", answer)
            print("label:", label)
            print("result:", label == answer)
        
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
        



# Example usage:
submission_file_path = r"practice\kickstart\2022\round_a\speed_typing.py"
problem_file_path = r"checker\sample_input.txt"
Checker(problem_file_path, submission_file_path).run()
