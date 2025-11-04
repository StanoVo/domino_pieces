from domino.base_piece import BasePiece
try:
    # prefer relative import when running as a package
    from .models import InputModel, OutputModel
except ImportError:
    # fallback to absolute import for editors or alternate import paths
    from domino_pieces.pieces.ZSVTest1Piece.models import InputModel, OutputModel
import pandas as pd
from pathlib import Path


class ZSVTest1Piece(BasePiece):
    
    def piece_function(self, input_data: InputModel):
        
        df_testdata = pd.read_csv(input_data.testdata_input_file)
    

        message = f"testdata readed successfully"
        file_path = str(Path(self.results_path) / "Test_Data_copied.csv")
        df_testdata.to_csv(file_path, index=False)

        # Set display result
        self.display_result = {
            "file_type": "csv",
            "file_path": file_path
        }

        # Return output
        return OutputModel(
            message=message,
            file_path=file_path
        )