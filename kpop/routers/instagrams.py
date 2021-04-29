from fastapi import APIRouter, Depends, HTTPException, Security
from datetime import datetime
from itertools import dropwhile, takewhile
import instaloader
from instascrape import Location 

from kpop.deps import authenticated
from kpop.config import settings

router = APIRouter(
    prefix="/instagrams",
    tags=["instagrams"],
    dependencies=[Security(authenticated)],
    responses={404: {"description": "Not found"}},
)

headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
           "cookie": f"sessionid={settings.INSTA_SESSION_ID};"}

@router.post("/instaload")
def instaload():
    bot = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(bot.context, 'python_scripts')
    print(type(profile))


@router.post("/instascrape")
def instascrape():
    url = 'https://www.instagram.com/explore/locations/212988663/new-york-new-york/'
    new_york = Location(url)
    new_york.scrape(headers=headers)
    print(f"The NY location tag has {new_york.amount_of_posts:,} posts")
    print(f"NY tag geographic coordinates: ({new_york.latitude}, {new_york.longitude}")