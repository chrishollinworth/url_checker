import aiohttp
import asyncio
import time



async def hit_api(session, tar):
    print(f"started hit_api at {time.strftime('%X')}")
    async with session.get(tar['url']) as response:
        await response.text()
    print (f"{tar['name']}  |||| {tar['url']} responded at {response.headers.get('Date')}.... data processing finished at {time.strftime('%X')}")



async def hit_api_group(sites):
    """
    this spawns a common session which is used to call the hit_api function
    
    """
    print(f"started hit_api_group at {time.strftime('%X')}")

    async with aiohttp.ClientSession() as session:
        return await asyncio.gather(*[hit_api(session, x) for x in sites]
                                         ,return_exceptions=True
                                         )

        

async def main(urls):
    print(f"started main at {time.strftime('%X')}")
    results= [asyncio.create_task(hit_api_group(urls))]
    await asyncio.gather(*results)

    print(results)

    print(f"finished at {time.strftime('%X')}")

def lambda_handler(event, context):
    
    additional_targets=event["additional_urls"]
    asyncio.run(main(additional_targets))