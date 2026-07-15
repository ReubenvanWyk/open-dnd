import random
import re
import sys

DICE = {"d3": 3, "d4": 4, "d6": 6, "d8": 8, "d10": 10, "d12": 12, "d20": 20, "d100": 100}

TOKEN_RE = re.compile(r"(\d*d\d+(?:kh\d+|kl\d+|dh\d+|dl\d+)?|[+-]|\d+)", re.IGNORECASE)

def roll_one(die, times=1):
    max_val = DICE.get(die)
    if not max_val:
        return None
    return [random.randint(1, max_val) for _ in range(times)]

def evaluate(expr):
    expr = expr.lower().replace(" ", "")
    tokens = TOKEN_RE.findall(expr)
    if not tokens:
        return None, "No dice expression found"

    total = 0
    parts = []
    sign = 1

    for token in tokens:
        if token == "+":
            sign = 1
        elif token == "-":
            sign = -1
        elif "d" in token:
            kh = re.search(r"kh(\d+)$", token)
            kl = re.search(r"kl(\d+)$", token)
            dh = re.search(r"dh(\d+)$", token)
            dl = re.search(r"dl(\d+)$", token)
            base = re.sub(r"(?:kh|kl|dh|dl)\d+$", "", token)

            if "d" not in base:
                return None, f"Invalid dice: {token}"

            count_str, die_name = base.split("d", 1)
            count = int(count_str) if count_str else 1
            die_key = f"d{die_name}"

            if die_key not in DICE:
                return None, f"Unknown die: d{die_name}"

            rs = roll_one(die_key, count)
            rolled_str = " ".join(map(str, rs))

            if kh:
                keep = int(kh.group(1))
                kept = sorted(rs, reverse=True)[:keep]
                s = sum(kept)
                sign_str = "+" if sign == 1 else "-"
                parts.append(f"{sign_str} {count}{die_key}({rolled_str})kh{keep}({'+'.join(map(str, kept))}={s})")
            elif kl:
                keep = int(kl.group(1))
                kept = sorted(rs)[:keep]
                s = sum(kept)
                sign_str = "+" if sign == 1 else "-"
                parts.append(f"{sign_str} {count}{die_key}({rolled_str})kl{keep}({'+'.join(map(str, kept))}={s})")
            elif dh:
                drop = int(dh.group(1))
                kept = sorted(rs)[:len(rs)-drop]
                s = sum(kept)
                sign_str = "+" if sign == 1 else "-"
                parts.append(f"{sign_str} {count}{die_key}({rolled_str})dh{drop}({'+'.join(map(str, kept))}={s})")
            elif dl:
                drop = int(dl.group(1))
                kept = sorted(rs, reverse=True)[:len(rs)-drop]
                s = sum(kept)
                sign_str = "+" if sign == 1 else "-"
                parts.append(f"{sign_str} {count}{die_key}({rolled_str})dl{drop}({'+'.join(map(str, kept))}={s})")
            else:
                s = sum(rs)
                sign_str = "+" if sign == 1 else "-"
                parts.append(f"{sign_str} {count}{die_key}({'+'.join(map(str, rs))}={s})")

            total += sign * s
        else:
            try:
                n = int(token)
                total += sign * n
                sign_str = "+" if sign == 1 else "-"
                parts.append(f"{sign_str} {n}")
            except ValueError:
                continue

    detail = " ".join(parts).lstrip("+ ")
    return total, detail

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Usage: python3 dice.py <expression>")
        print("Examples:")
        print("  python3 dice.py d20")
        print("  python3 dice.py 2d6+3")
        print("  python3 dice.py d20+5-2")
        print("  python3 dice.py 2d20kh1     (advantage)")
        print("  python3 dice.py 2d20kl1     (disadvantage)")
        print("  python3 dice.py d20+5-2d4")
        sys.exit(1)

    for expr in args:
        result, detail = evaluate(expr)
        if result is None:
            print(f"Error: {detail}")
        else:
            print(f"{expr} = {detail} = {result}")
