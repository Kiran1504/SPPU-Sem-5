class Tables:
    def __init__(self) -> None:
        self.id = int
        self.notation = ''
        self.mem_loc = int

    def add_entry_to_table(self, id, notation):
        self.id = id
        self.notation = notation
    
    def assign_memory(self, loc):
        self.mem_loc = loc
    
class Assembler:
    def __init__(self) -> None:
        self.input_code = []
        self.intermediate_code = []
        self.symbol_table = []
        self.literal_table = []
        self.pool_table = []
        self.program_started = False
        self.program_ended = False
    
    def read_file(self):
        with open("code1.txt", "r") as file:
            code = file.read()
            code_lines = code.splitlines()
            for code_line in code_lines:
                self.input_code.append(code_line.split(" "))
    
    def tokenization(self):
        for line in self.input_code:
            pass

obj = Assembler()
obj.read_file()