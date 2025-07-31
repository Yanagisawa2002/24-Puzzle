import sys

def solve_24(numbers, expressions):
    if len(numbers) == 1:
        if abs(numbers[0] - 24) < 1e-6:
            return expressions[0]
        else:
            return None
    
    n = len(numbers)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            a = numbers[i]
            b = numbers[j]
            expr_a = expressions[i]
            expr_b = expressions[j]
            
            # 创建新的数字列表和表达式列表，排除i和j
            new_numbers = []
            new_expressions = []
            for k in range(n):
                if k != i and k != j:
                    new_numbers.append(numbers[k])
                    new_expressions.append(expressions[k])
            
            # 尝试所有运算符
            for op in ['+', '-', '*', '/']:
                if op == '/' and b == 0:
                    continue  # 避免除零错误
                
                # 计算结果
                if op == '+':
                    result = a + b
                elif op == '-':
                    result = a - b
                elif op == '*':
                    result = a * b
                else:  # '/'
                    if b == 0:
                        continue
                    result = a / b
                
                # 格式化表达式
                new_expr = f"({expr_a}{op}{expr_b})"
                
                # 递归调用
                solution = solve_24(new_numbers + [result], new_expressions + [new_expr])
                if solution is not None:
                    return solution
    
    return None

def main():
    if len(sys.argv) > 1:
        # 从命令行参数获取数字
        try:
            nums = list(map(float, sys.argv[1:5]))
            if len(nums) !=4:
                print("请输入四个数字")
                return
        except ValueError:
            print("请输入有效的数字")
            return
    else:
        # 交互式输入
        while True:
            input_str = input("请输入四个数字，用空格分隔：")
            nums = input_str.split()
            if len(nums) !=4:
                print("请输入四个数字")
                continue
            try:
                nums = list(map(float, nums))
                break
            except ValueError:
                print("请输入有效的数字")
    
    # 格式化初始表达式
    def format_num(n):
        if n.is_integer():
            return str(int(n))
        else:
            return str(n)
    
    initial_expressions = [format_num(num) for num in nums]
    solution = solve_24(nums, initial_expressions)
    
    if solution:
        print(f"可以解决：{solution}")
    else:
        print("无法解决")

if __name__ == "__main__":
    main()
