from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Test Meteo Data Piece Input Model
    """
    data_input_folder: str = Field(
        title="Path to folder with input data",
        # default='/home/shared_storage/',
        description="The path to folder with input meteo data files "
    )    

    data_input_file: str = Field(
        title="Input data file name",
        # File.doc',
        description="Name of the word doc with meteo data"        
    )

    data_output_folder: str = Field(
        title="Path to folder with output data",
        # default='????',
        description="The path to folder with output meteo data files "
    )
    data_output_file: str = Field(
        title="Output data file name",
        # File.csv',
        description="Name of the CSV file with meteo data"
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
        description="The path & file name to the output CSV file"
    )
    
    
