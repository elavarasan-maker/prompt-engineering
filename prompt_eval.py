import json
def validate_classification(raw):
 data=json.loads(raw)
 if data.get("label") not in {"request","complaint","feedback","other"}: raise ValueError("Invalid label")
 if data.get("confidence") not in {"low","medium","high"}: raise ValueError("Invalid confidence")
 if not isinstance(data.get("evidence"),str): raise ValueError("evidence must be text")
 return data
def exact_match(expected,actual): return expected.strip().casefold()==actual.strip().casefold()
if __name__=="__main__":
 print(validate_classification('{"label":"feedback","confidence":"medium","evidence":"The page is confusing"}'))
