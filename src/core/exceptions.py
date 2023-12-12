from fastapi import HTTPException, status

item_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Item not found",
)
