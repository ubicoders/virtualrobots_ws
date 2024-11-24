from ubicoders_vrobots.vrobots_bridge.vr_main_srv import run_servers
import asyncio


if __name__ == "__main__":
    asyncio.run(run_servers())