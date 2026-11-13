# Сколько минут выступления «Суровый Питерский форум» уже использовано в роликах (лимит по договору — 20 мин).
# Запуск из корня репозитория: python3 instagram/edits/talk_usage.py
import json, glob, os
LIMIT = 20 * 60
tot = 0
for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), 'sp*', 'edit-decisions.json'))):
    d = sum(c['end'] - c['start'] for c in json.load(open(f))['cuts'])
    tot += d
    print(f"{os.path.basename(os.path.dirname(f)).upper():6} {d:6.1f} с")
print(f"ИТОГО  {tot:6.1f} с = {int(tot//60)} мин {int(tot%60):02d} с из 20:00 · осталось {int((LIMIT-tot)//60)} мин {int((LIMIT-tot)%60):02d} с")
