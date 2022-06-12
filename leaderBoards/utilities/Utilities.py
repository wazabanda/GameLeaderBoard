import uuid


def generateToken(userName:str,boardName:str,postId:str) -> str:
    """
    _summary_
    Generate a token based on user name and board name and id
    """
    tempToken = str(uuid.uuid4())

    token = userName + "-:-" + boardName + "::" + tempToken +"-" + postId
    token = token.replace(" ","-")
    return token
    