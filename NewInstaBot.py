from instapy import InstaPy

session = InstaPy(username = "" , password = "")
session.login()

session.set_relationship_bounds(enabled = True, max_followers = 200)

session.set_do_follow(True, percentage=50)
session.like_by_tags([""], amount = 3 )
session.set_dont_like([""])

#session.unfollow_users(amount=6, allFollowing=True, sleep_delay=60)

session.end()
