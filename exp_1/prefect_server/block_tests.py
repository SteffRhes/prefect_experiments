from prefect.filesystems import LocalFileSystem

local_file_system_block = LocalFileSystem.load("block-files-test-1")
