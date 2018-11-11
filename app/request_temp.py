import os
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def web_hook():
    res = ''
    if request.method == 'GET':
        return "Hello!"
    req = request.get_json(silent=True, force=True)
    try:
        action = req.get('queryResult').get('intent').get('displayName')
    except AttributeError:
        return 'error'
    if action == "welcome":
        res = make_response(jsonify({'fulfillmentText': 'Welcome to the Hackathon! Is this your first time?'}))
    elif action == "welcome-yes":
        res = make_response(jsonify({'fulfillmentText': "What programming language will you use?"}))
    elif action == "welcome-no":
        res = make_response(jsonify({'fulfillmentText': "Ok, see you next year."}))
    elif action == "programming":
        plang = req.get('queryResult').get('outputContexts')[0].get('parameters').get('plang')
        res = make_response(jsonify({'fulfillmentText': "Nice! I also love {}! See you!".format(plang)}))
    # elif action == "get_listing":
    #     res = make_response(jsonify({'fulfillmentText': "We've got the listings for you! "
    #                                                     "There are {} houses available! "
    #                                                     "Do you have any preferences for your new home?".format(hd.get_list_count())}))
    # elif action == "const_location":
    #     if req['queryResult'].get('allRequiredParamsPresent'):
    #         if req['queryResult']['parameters']['geo-city'] in hd.city_set:
    #             hd.city = req['queryResult']['parameters']['geo-city']
    #             hd.city_const()
    #             res = make_response(jsonify(
    #                 {'fulfillmentText': "I am glad you choose {}! There are {} resources."
    #                     .format(hd.city, hd.get_new_list_count())}))
    #         else:
    #             res = make_response(jsonify(
    #                 {'fulfillmentText': "Sorry we don't have any resources in {}."
    #                     .format(req['queryResult']['parameters']['geo-city'])}))
    #     else:
    #         res = make_response(jsonify({'fulfillmentText': "I am sorry. Can you tell me which city in MA you prefer?"}))
    # elif action == 'const_beds':
    #     if req['queryResult'].get('allRequiredParamsPresent'):
    #         if req['queryResult']['parameters']['number'] in hd.beds_num_set:
    #             hd.beds = int(req['queryResult']['parameters']['number'])
    #             hd.beds_const()
    #             res = make_response(jsonify(
    #                 {'fulfillmentText': "Good choice! Let me get you a list of houses with {} bedrooms. "
    #                                     "There are {} resources".format(int(hd.beds), hd.get_new_list_count())}))
    #         else:
    #             res = make_response(jsonify(
    #                 {'fulfillmentText': "Sorry we don't have any houses have {} bedrooms."
    #                     .format(int(req['queryResult']['parameters']['number']))}
    #             ))
    #     else:
    #         res = make_response(jsonify({'fulfillmentText': "How many bedrooms do you want?"}))
    # elif action == 'const_price':
    #     hd.price_op = req['queryResult']['parameters']['comp']
    #     hd.price2 = req['queryResult']['parameters']['unit-currency2'].get('amount')
    #     if hd.price_op == 'between':
    #         hd.price1 = req['queryResult']['parameters']['unit-currency1'].get('amount')
    #     hd.price_const()
    #     res = make_response(jsonify({'fulfillmentText': 'No problem! We will choose the best deal for you! '
    #                                                     'There are {} resources.'.format(hd.get_new_list_count())}))
    # elif action == "re_listing":
    #     hd.new_listings()
    #     res = make_response(jsonify({'fulfillmentText': "I have got the listing! There are {} houses "
    #                                                     "meet your requirements. "
    #                                                     "Do you have any further questions?".format(hd.get_new_list_count())}))
    # elif action == "re_listing-yes":
    #     res = make_response(jsonify({'fulfillmentText': "the house is in {} with {} bedrooms. Any other questions?"
    #                                 .format(hd.city, hd.beds)}))
    # elif action == "re_listing-no":
    #     res = make_response(jsonify({'fulfillmentText': "Thank you so much! I will email you the listings! Have a good day!"}))
    #     hd.reset()
    # elif action == "get_listing-fallback":
    #     res = make_response(jsonify({'fulfillmentText': 'I am sorry. Do you have any preferences about the houses?'}))
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))