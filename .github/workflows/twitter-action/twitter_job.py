"""
This file should be only run at GitHub action, when the publication/ref.bib is
changed.

We expect the change to be a new entry of publication, for example:

@unpublished{test,
  author    = {Nuri Cingillioglu and Alessandra Russo},
  title     = {{pix2rule: End-to-end Neuro-symbolic Rule Learning}},
  journal   = {CoRR},
  volume    = {abs/2106.07487},
  year      = {2021},
  url       = {https://arxiv.org/abs/2106.07487},
  _code     = {https://github.com/nuric/pix2rule}
  _tags     = {neuro-symbolic reasoning, end-to-end learning, relational representations}
}

The author, title, url and _tags are essential for this script to run properly.

During GitHub action, the changed lines would be written in a file named
`changes.txt`, and we will be reading from this file to extract contents for the
new tweet.
"""
import os
import re

import tweepy


def generate_twitter_tag(og_tag: str) -> str:
    """
    Change a tag string to a twitter tag string
    Example: neuro-symbolic learning -> #NeuroSymbolicLearning
    """
    splited_tag = re.split("-| ", og_tag)
    twitter_tag = "#" + "".join([s.title() for s in splited_tag])
    return twitter_tag


# Get twitter keys
TWITTER_APP_KEY = os.environ["TWITTER_APP_KEY"]
TWITTER_APP_SECRET = os.environ["TWITTER_APP_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]

# Verification
auth = tweepy.OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
print("Twitter verified")

with open("changes.txt", "r") as f:
    changed_str = f.read()

# Get author
raw_authors = re.findall(r"author *= *\{+([^\{\}]*)\}+", changed_str)[0]
author = re.split(" and ", raw_authors)[0] + " et al."

# Get title
title = re.findall(r"title *= *\{+([^\{\}]*)\}+", changed_str)[0]

# Get paper url
url = re.findall(r"url *= *\{+([^\{\}]*)\}+", changed_str)[0]

# Generate twitter tags
raw_tags_match = re.findall(r"_tags *= *\{+([^\{\}]*)\}+", changed_str)
if len(raw_tags_match) != 1 or raw_tags_match[0] == None:
    twitter_tags = []
else:
    tags = re.split(", |,", raw_tags_match[0])
    twitter_tags = [generate_twitter_tag(t) for t in tags]

# Post content
post_content = f"Checkout this new paper '{title}' at {url}, by {author}.\n"
if len(post_content) > 280:
    # Add ... if the post without any tag is already too long
    post_content = post_content[:277] + "..."
else:
    # Try to add all the tags, if too long, remove one tag and try again
    for i in range(len(twitter_tags)):
        post_tag = " ".join(twitter_tags[: len(twitter_tags) - i])
        if len(post_content + post_tag) <= 280:
            post_content += post_tag
            break

# post
try:
    response = api.update_status(post_content, tweet_mode="extended")
    if response.full_text != None:
        print(
            "Successfully post the tweet:\n===================\n"
            + response.full_text
            + "\n==================="
        )
except ValueError as err:
    print("There's an error posting tweet")
    print(err)
