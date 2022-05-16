def arithmetic_arranger(problems, answer_ok=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = str()
    sumas_result = list()
    sumandos_sup = list()
    sumandos_inf = list()
    linea = list()

    for problem in problems:
        try:
            sum1, op, sum2 = problem.split()
        except ValueError as e:
            print(e)
            return 'Format is "num1[blankSpace][operator][blankSpace]num2" eg. "num1 + num2" or "num1 - num2" '
        except AttributeError:
            return "Problem can't be None"
        except Exception:
            return "I don't know Rick"
        if not (sum1.isdigit()) or not (sum2.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(sum1) > 4 or len(sum2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if op not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'"
        espaciado = max(len(sum1), len(sum2))
        sumandos_sup.append("{: >{esp}}".format(sum1, esp=espaciado + 2))
        sumandos_inf.append(op + "{: >{esp}}".format(sum2, esp=espaciado + 1))
        linea.append("{:->{width}s}".format("", width=espaciado + 2))
        sumas_result.append("{: >{esp}}".format(eval(problem), esp=espaciado + 2))

    # sum_output1
    sum_output1 = ""
    for sum_sup in sumandos_sup:
        sum_output1 += sum_sup + "\t"
    # sum_output2
    sum_output2 = ""
    for sum_inf in sumandos_inf:
        sum_output2 += sum_inf + "\t"
    # sum_output3line
    sum_output3line = ""
    for sum_line in linea:
        sum_output3line += sum_line + "\t"
    # sum_output4_result
    sum_output4_result = ""
    for sum_result in sumas_result:
        sum_output4_result += sum_result + "\t"

    arranged_problems = (
        sum_output1
        + "\n"
        + sum_output2
        + "\n"
        + sum_output3line
        + (("\n" + sum_output4_result) if answer_ok else "")
    )

    return arranged_problems
