from src.main import main
def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello Template" in captured.out