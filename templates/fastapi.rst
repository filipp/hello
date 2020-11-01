#!/usr/bin/env python

import subprocess

import fastapi

app = fastapi.FastAPI()


def main():
  args = ["uvicorn", "main:app", "--reload"]
  subprocess.call(args)

if __name__ == '__main__':
  main()
