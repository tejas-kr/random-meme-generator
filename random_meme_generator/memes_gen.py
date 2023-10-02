from flask import current_app, Blueprint, request, abort
from meme_url_grabber import Meme


memes_gen = Blueprint('memes_gen', __name__)

@memes_gen.route('/memes', methods=["GET"])
def get_random_memes():
    """get_random_memes

    Returns:
        json: Response
    """
    try: 
        if request.args.get('count') and request.args.get('count').isdigit():
            memes = Meme(logger=current_app.logger, count=int(request.args.get('count'))).get_memes()
        else: 
            memes = Meme(logger=current_app.logger).get_memes()
        memes_dict = {
            num: {'text': item[0], 'link': item[1]}
            for num, item in enumerate(memes, start=1)
        }
        current_app.logger.info(f"Memes grabbed::{memes_dict}")
        return memes_dict
    except Exception as e:
        current_app.logger.error(e)
        abort(404, "Memes Not found")