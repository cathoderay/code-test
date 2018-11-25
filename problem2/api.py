import json
from falcon import API, HTTP_200, HTTP_400 

from problem2 import solve


class CalculatorAPI:
    def on_post(self, req, resp):
        try:
            expr = json.load(req.stream)['expression']
        except KeyError:
            result = "missing 'expression' key"
            resp.status = HTTP_400
        else:
            try:
                result = str(solve(expr))
                resp.status = HTTP_200
            except ZeroDivisionError:
                result = "division by zero"
                resp.status = HTTP_400 
            except Exception:
                result = "error"
                resp.status = HTTP_400

        resp.body = json.dumps({"result": result})


api = API()
api.add_route('/calc', CalculatorAPI())
