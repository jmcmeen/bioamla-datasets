#!/usr/bin/env python3
import argparse
from datasets import load_dataset


def push_dataset(source: str, destination: str) -> None:
    """Load a dataset from source and push it to the Hugging Face Hub."""
    dataset = load_dataset(source)
    dataset.push_to_hub(destination)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Push a local dataset to the Hugging Face Hub"
    )
    parser.add_argument(
        "source",
        help="Path to the local dataset directory",
    )
    parser.add_argument(
        "destination",
        help="Hugging Face Hub repository (e.g., 'username/dataset-name')",
    )
    args = parser.parse_args()

    push_dataset(args.source, args.destination)


if __name__ == "__main__":
    main()
