from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Test Meteo Data Piece Input Model
    """

    data_input_file: str = Field(
        title="Input data",
        # default='/home/shared_storage/File.doc',
        description="The path to the input meteo data in word doc file"
    )


class OutputModel(BaseModel):
    """
    Test Meteo Data Piece Output Model
    """
    message: str = Field(
        default="",
        description="Output message to log"
    )

    file_path: str = Field(
        description="The path to the output CSV data file"
    )
