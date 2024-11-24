from ubicoders_vrobots import main_graph_runner
import asyncio


if __name__ == "__main__":
    asyncio.run(main_graph_runner(
        backend="pyqt",
        data_length=50*30,
        interval=250
    ))