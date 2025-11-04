from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Test Data Piece Input Model
    """

    testdata_input_file: str = Field(
        title="Test input data",
        # default='/home/shared_storage/TestData.csv',
        description="The path to the Test Data",
    )


class OutputModel(BaseModel):
    """
    Test Data Piece Output Model
    """
    message: str = Field(
        default="",
        description="Output message to log"
    )

    file_path: str = Field(
        description="The path to the copied Test Data file by the specified Location"
    )
